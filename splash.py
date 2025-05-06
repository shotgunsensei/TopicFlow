from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QTimer
from ui.home import HomeScreen

import os


class SplashScreen(QMainWindow):
    """
    This class handles the splash screen shown at app launch.
    Displays the TopicFlow logo and a welcome message.
    After a short delay, it transitions to the HomeScreen.
    """

    def __init__(self):
        super().__init__()

        # Set window title and fixed size
        self.setWindowTitle("TopicFlow - Starting...")
        self.setFixedSize(500, 300)

        # Center the window on screen (roughly)
        self.move(400, 200)

        # Initialize the splash screen UI
        self.init_ui()

        # After 2 seconds, switch to Home screen
        QTimer.singleShot(2000, self.show_home)

    def init_ui(self):
        """
        Sets up the logo and welcome text in the splash screen.
        """
        logo_path = os.path.join("assets", "topicflow_logo.png")

        # Display the logo
        self.logo = QLabel(self)
        pixmap = QPixmap(logo_path)
        self.logo.setPixmap(pixmap.scaled(120, 120, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setGeometry(190, 40, 120, 120)

        # Display welcome text
        self.text = QLabel("Welcome to TopicFlow", self)
        self.text.setAlignment(Qt.AlignCenter)
        self.text.setFont(QFont("Segoe UI", 14))
        self.text.setGeometry(100, 180, 300, 40)

    def show_home(self):
        """
        Closes the splash screen and opens the main home screen.
        """
        self.home = HomeScreen()
        self.home.show()
        self.close()
