import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QFrame, QTableWidget, QTableWidgetItem, QHeaderView, 
    QAbstractItemView, QPushButton
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Панель управления")
        self.resize(1100, 700)
        self.setStyleSheet("background-color: white; color: black;")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(28, 20, 28, 24)
        main_layout.setSpacing(20)

        logo = QFrame()
        logo.setFrameShape(QFrame.Shape.Box)
        logo.setMinimumHeight(70)
        logo.setStyleSheet("QFrame { border: 1px solid black; } QLabel { border: none; }")
        logo_layout = QHBoxLayout(logo)
        logo_layout.addWidget(QLabel("Логотип организации"))
        logo_layout.addStretch()
        main_layout.addWidget(logo)

        heading_layout = QHBoxLayout()
        heading = QLabel("Панель управления")
        heading.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        heading_layout.addWidget(heading)
        heading_layout.addStretch()

        for period in ["Сегодня", "Неделя", "Месяц", "Квартал"]:
            btn = QPushButton(period)
            btn.setFlat(True) 
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setStyleSheet("""
                QPushButton { border: none; background: transparent; font-size: 14px; }
                QPushButton:hover { color: blue; text-decoration: underline; }
            """)
            btn.clicked.connect(lambda checked, p=period: print(f"Выбран период: {p}"))
            heading_layout.addWidget(btn)

        main_layout.addLayout(heading_layout)

        cards_layout = QGridLayout()
        cards_layout.setSpacing(8)

        cards_data = [
            ("Участники", "2"),
            ("Взносы", "35 000 ₽"),
            ("Мероприятия", "3"),
            ("Голосования", "2")
        ]

        for index, (title, value) in enumerate(cards_data):
            card = QPushButton()
            card.setMinimumHeight(70)
            card.setMinimumWidth(300)
            card.setCursor(Qt.CursorShape.PointingHandCursor)
            card.setStyleSheet("""
                QPushButton { 
                    border: 1px solid black; 
                    background-color: white; 
                    text-align: left; 
                    padding: 10px;
                }
                QPushButton:hover { background-color: #f0f0f0; }
            """)
            
            card_layout = QHBoxLayout(card)
            
            title_label = QLabel(title)
            card_layout.addWidget(title_label)
            card_layout.addStretch()

            value_label = QLabel(value)
            value_label.setFont(QFont("Arial", 11, QFont.Weight.Bold))
            card_layout.addWidget(value_label)

                       # При клике проверяем, какая карточка нажата
            def on_card_clicked(checked=False, card_title=title):
                if card_title == "Участники":
                    from participants import ParticipantsWindow
                    self.participants_window = ParticipantsWindow()
                    self.participants_window.show()
                    self.close()
                else:
                    print(f"Переход в раздел: {card_title} (в разработке)")

            card.clicked.connect(on_card_clicked)

            cards_layout.addWidget(card, index // 2, index % 2)

        main_layout.addLayout(cards_layout)

        actions_label = QLabel("Последние действия")
        actions_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        actions_label.setStyleSheet("background-color: #d0d0d0; padding: 7px; border: 1px solid #a0a0a0;")
        main_layout.addWidget(actions_label)

        self.table = QTableWidget()
        self.table.setColumnCount(1)
        self.table.setHorizontalHeaderLabels(["Действие"])

        actions = ["Добавлен новый участник", "Создано голосование", "Внесён взнос"]
        self.table.setRowCount(len(actions))

        for row, action in enumerate(actions):
            item = QTableWidgetItem(action)
            item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(row, 0, item)

        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setStretchLastSection(False)
        self.table.verticalHeader().setDefaultSectionSize(35)
        self.table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.setFixedHeight(130) 
        main_layout.addWidget(self.table)
        main_layout.addStretch()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec())