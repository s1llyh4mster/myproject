import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QLineEdit, QPushButton, QFrame, QTableWidget, 
    QTableWidgetItem, QHeaderView, QComboBox, QAbstractItemView
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class ParticipantsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Список участников")
        self.resize(1100, 700)
        self.setStyleSheet("background-color: white; color: black;")

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        logo = QFrame()
        logo.setFrameShape(QFrame.Shape.Box)
        logo.setMinimumHeight(60)
        logo.setStyleSheet("border: 1px solid black;")
        logo_layout = QHBoxLayout(logo)
        logo_layout.addWidget(QLabel("Logo"))
        logo_layout.addStretch()
        layout.addWidget(logo)

        self.back_btn = QPushButton("← Назад к панели управления")
        self.back_btn.setFlat(True)
        self.back_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.back_btn.setStyleSheet("text-align: left; color: black; font-size: 14px; border: none;")
        self.back_btn.clicked.connect(self.go_back)
        layout.addWidget(self.back_btn)

        filter_layout = QHBoxLayout()
        
        title = QLabel("Участники")
        title.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        filter_layout.addWidget(title)
        filter_layout.addSpacing(20)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Поиск по имени или email...")
        self.search_input.setFixedWidth(250)
        self.search_input.setMinimumHeight(30)
        self.search_input.setStyleSheet("border: 1px solid black; padding: 5px;")
        filter_layout.addWidget(self.search_input)

        self.status_combo = QComboBox()
        self.status_combo.addItems(["Статус", "Активен", "Неактивен", "Приостановлен"])
        self.status_combo.setFixedWidth(120)
        self.status_combo.setStyleSheet("border: 1px solid black; padding: 5px;")
        filter_layout.addWidget(self.status_combo)

        self.role_combo = QComboBox()
        self.role_combo.addItems(["Роль", "Админ", "Участник"])
        self.role_combo.setFixedWidth(120)
        self.role_combo.setStyleSheet("border: 1px solid black; padding: 5px;")
        filter_layout.addWidget(self.role_combo)

        self.date_input = QLineEdit()
        self.date_input.setPlaceholderText("от 01.01.25 до 31.12.25")
        self.date_input.setFixedWidth(200)
        self.date_input.setMinimumHeight(30)
        self.date_input.setStyleSheet("border: 1px solid black; padding: 5px;")
        filter_layout.addWidget(self.date_input)

        filter_layout.addStretch()

        self.add_btn = QPushButton("+ Новый участник")
        self.add_btn.setMinimumHeight(35)
        self.add_btn.setStyleSheet("border: 1px solid black; padding: 5px 10px; background-color: white;")
        self.add_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        filter_layout.addWidget(self.add_btn)

        layout.addLayout(filter_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ФИО", "Email", "Роль", "Статус", "Дата вступления", "Действия"])
        
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.verticalHeader().setVisible(False)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setStyleSheet("QTableWidget { gridline-color: gray; border: 1px solid black; }")
        
        self.load_data()
        layout.addWidget(self.table)

        pagination_layout = QHBoxLayout()
        pagination_layout.addWidget(QLabel("< 1 >"))
        pagination_layout.addStretch()
        pagination_layout.addWidget(QLabel("Страница 1 из 1"))
        layout.addLayout(pagination_layout)

    def load_data(self):
        data = [
            ("Иванов Иван Иванович", "ivan@mail.ru", "Администратор", "Активен", "01.01.2025"),
            ("Ромашкина Мария Евгеньевна", "mariya@mail.ru", "Участник", "Активен", "01.02.2025")
        ]
        self.table.setRowCount(len(data))
        for row, (fio, email, role, status, date) in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(fio))
            self.table.setItem(row, 1, QTableWidgetItem(email))
            self.table.setItem(row, 2, QTableWidgetItem(role))
            self.table.setItem(row, 3, QTableWidgetItem(status))
            self.table.setItem(row, 4, QTableWidgetItem(date))
            
            action_widget = QWidget()
            action_layout = QHBoxLayout(action_widget)
            action_layout.setContentsMargins(0, 0, 0, 0)
            
            btn_open = QPushButton("Открыть")
            btn_edit = QPushButton("Изменить")
            btn_del = QPushButton("Удалить")
            
            for btn in [btn_open, btn_edit, btn_del]:
                btn.setFlat(True)
                btn.setCursor(Qt.CursorShape.PointingHandCursor)
                btn.setStyleSheet("color: #2F6FED; text-decoration: underline; border: none; background: transparent;")
                action_layout.addWidget(btn)
                
            self.table.setCellWidget(row, 5, action_widget)

    def go_back(self):
        from dashboard import Dashboard
        self.dashboard = Dashboard()
        self.dashboard.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ParticipantsWindow()
    window.show()
    sys.exit(app.exec())