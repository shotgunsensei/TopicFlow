from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

import os


class SplashScreen(QMainWindow):
    """
    This class handles the splash screen shown at app launch.
    Displays the TopicFlow logo and welcome message.
    """

    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("TopicFlow - Starting...")
        self.setFixedSize(500, 300)

        # Center the window on screen
        self.move(400, 200)

        # Setup UI Elements
        self.init_ui()

    def init_ui(self):
        # Path to logo image in assets folder
        logo_path = os.path.join("assets", "topicflow_logo.png")

        # Logo image
        self.logo = QLabel(self)
        pixmap = QPixmap(logo_path)
        self.logo.setPixmap(pixmap.scaled(120, 120, Qt.KeepAspectRatio))
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setGeometry(190, 40, 120, 120)

        # Welcome text
        self.text = QLabel("Welcome to TopicFlow", self)
        self.text.setAlignment(Qt.AlignCenter)
        self.text.setFont(QFont("Segoe UI", 14))
        self.text.setGeometry(100, 180, 300, 40)
