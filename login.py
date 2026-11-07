import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, 
    QLineEdit, QPushButton, QFrame, QHBoxLayout, QCheckBox, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from dashboard import Dashboard 

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вход в систему")
        self.resize(400, 650)
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

        heading = QLabel("Вход в систему")
        heading.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(heading)

        layout.addWidget(QLabel("Email"))
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Введите email")
        self.email_input.setMinimumHeight(40)
        self.email_input.setStyleSheet("border: 1px solid black; padding: 5px;")
        layout.addWidget(self.email_input)

        layout.addWidget(QLabel("Пароль"))
        
        password_layout = QHBoxLayout()
        password_layout.setSpacing(0)
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Введите пароль")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setMinimumHeight(40)
        self.password_input.setStyleSheet("border: 1px solid black; border-right: none; padding: 5px;")
        
        self.toggle_password_btn = QPushButton("👁")
        self.toggle_password_btn.setFixedSize(40, 40)
        self.toggle_password_btn.setStyleSheet("border: 1px solid black; background-color: white;")
        self.toggle_password_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.toggle_password_btn.clicked.connect(self.toggle_password)
        
        password_layout.addWidget(self.password_input)
        password_layout.addWidget(self.toggle_password_btn)
        layout.addLayout(password_layout)

        self.error_label = QLabel("Неверный логин или пароль")
        self.error_label.setStyleSheet("color: red; border: none;")
        self.error_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.error_label.hide()
        layout.addWidget(self.error_label)

        row = QHBoxLayout()
        self.checkbox = QCheckBox("Запомнить меня")
        row.addWidget(self.checkbox)
        row.addStretch()
        forgot_link = QLabel("Забыли пароль?")
        forgot_link.setStyleSheet("color: gray; border: none;")
        row.addWidget(forgot_link)
        layout.addLayout(row)

        self.login_btn = QPushButton("Войти")
        self.login_btn.setMinimumHeight(45)
        self.login_btn.setStyleSheet("background-color: #E0E0E0; border: 1px solid black; font-weight: bold; font-size: 14px;")
        self.login_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.login_btn.clicked.connect(self.check_login)
        layout.addWidget(self.login_btn)

        self.register_link = QPushButton("Нет аккаунта? Зарегистрироваться")
        self.register_link.setFlat(True) 
        self.register_link.setCursor(Qt.CursorShape.PointingHandCursor)
        self.register_link.setStyleSheet("border: none; color: gray; background: transparent;")
        self.register_link.clicked.connect(self.open_register)
        layout.addWidget(self.register_link, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addStretch()

    def toggle_password(self):
        if self.password_input.echoMode() == QLineEdit.EchoMode.Password:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
            self.toggle_password_btn.setText("🔒")
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
            self.toggle_password_btn.setText("👁")

    def check_login(self):
        email = self.email_input.text()
        password = self.password_input.text()

        if email == "admin" and password == "123":
            self.error_label.hide()
            self.email_input.setStyleSheet("border: 1px solid black; padding: 5px;")
            self.password_input.setStyleSheet("border: 1px solid black; border-right: none; padding: 5px;")
            
            self.dashboard = Dashboard()
            self.dashboard.show()
            self.close()
        else:
            self.error_label.show()
    
    def open_register(self):
        from register import RegisterWindow
        
        self.register_window = RegisterWindow()
        self.register_window.show()
        self.close() 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())