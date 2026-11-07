import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, 
    QLineEdit, QPushButton, QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class RegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Регистрация")
        self.resize(400, 750)
        self.setStyleSheet("background-color: white; color: black;")

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(40, 30, 40, 30)
        layout.setSpacing(15)

        logo_frame = QFrame()
        logo_frame.setStyleSheet("border: 1px solid black;")
        logo_layout = QVBoxLayout(logo_frame)
        logo_layout.setContentsMargins(20, 20, 20, 20)
        
        logo_icon_frame = QFrame()
        logo_icon_frame.setStyleSheet("border: 1px solid black;")
        logo_icon_frame.setFixedSize(80, 50)
        logo_icon_layout = QVBoxLayout(logo_icon_frame)
        logo_icon_layout.setContentsMargins(0, 0, 0, 0)
        logo_label = QLabel("Logo")
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo_icon_layout.addWidget(logo_label)
        
        title = QLabel("Система\nуправления\nчленством в НКО")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        logo_layout.addWidget(logo_icon_frame, alignment=Qt.AlignmentFlag.AlignHCenter)
        logo_layout.addWidget(title)
        layout.addWidget(logo_frame)

        heading = QLabel("Регистрация")
        heading.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(heading)

        layout.addWidget(QLabel("Имя *"))
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Введите имя")
        self.name_input.setMinimumHeight(40)
        self.name_input.setStyleSheet("border: 1px solid black; padding: 5px;")
        layout.addWidget(self.name_input)

        layout.addWidget(QLabel("Фамилия *"))
        self.surname_input = QLineEdit()
        self.surname_input.setPlaceholderText("Введите фамилию")
        self.surname_input.setMinimumHeight(40)
        self.surname_input.setStyleSheet("border: 1px solid black; padding: 5px;")
        layout.addWidget(self.surname_input)

        layout.addWidget(QLabel("Отчество (необязательно)"))
        self.midname_input = QLineEdit()
        self.midname_input.setPlaceholderText("Введите отчество")
        self.midname_input.setMinimumHeight(40)
        self.midname_input.setStyleSheet("border: 1px solid black; padding: 5px;")
        layout.addWidget(self.midname_input)

        layout.addWidget(QLabel("Email *"))
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Введите email")
        self.email_input.setMinimumHeight(40)
        self.email_input.setStyleSheet("border: 1px solid black; padding: 5px;")
        layout.addWidget(self.email_input)

        layout.addWidget(QLabel("Пароль *"))
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Введите пароль")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setMinimumHeight(40)
        self.password_input.setStyleSheet("border: 1px solid black; padding: 5px;")
        layout.addWidget(self.password_input)

        layout.addWidget(QLabel("Подтверждение пароля *"))
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setPlaceholderText("Введите пароль еще раз")
        self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_password_input.setMinimumHeight(40)
        self.confirm_password_input.setStyleSheet("border: 1px solid black; padding: 5px;")
        layout.addWidget(self.confirm_password_input)

        self.register_btn = QPushButton("Зарегистрироваться")
        self.register_btn.setMinimumHeight(45)
        self.register_btn.setStyleSheet("background-color: #E0E0E0; border: 1px solid black; font-weight: bold; font-size: 14px;")
        self.register_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        layout.addWidget(self.register_btn)

        self.back_btn = QPushButton("Уже есть аккаунт? Войти")
        self.back_btn.setFlat(True)
        self.back_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.back_btn.setStyleSheet("border: none; color: gray; background: transparent;")
        self.back_btn.clicked.connect(self.open_login)
        layout.addWidget(self.back_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        
        layout.addStretch()
    
    def open_login(self):
        from login import LoginWindow
        
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterWindow()
    window.show()
    sys.exit(app.exec())