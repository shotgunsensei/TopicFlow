from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QTimer
from ui.home import HomeScreen
import os

class SplashScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TopicFlow - Starting...")
        self.setFixedSize(500, 300)
        self.move(400, 200)
        self.init_ui()
        QTimer.singleShot(2000, self.show_home)

    def init_ui(self):
        logo_path = os.path.join("assets", "topicflow_logo.png")

        self.logo = QLabel(self)
        pixmap = QPixmap(logo_path)
        self.logo.setPixmap(pixmap.scaled(120, 120, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setGeometry(190, 40, 120, 120)

        self.text = QLabel("Welcome to TopicFlow", self)
        self.text.setAlignment(Qt.AlignCenter)
        self.text.setFont(QFont("Segoe UI", 14))
        self.text.setGeometry(100, 180, 300, 40)

    def show_home(self):
        self.home = HomeScreen()
        self.home.show()
        self.close()
