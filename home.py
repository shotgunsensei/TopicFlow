from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class HomeScreen(QMainWindow):
    """
    This class handles the main home window that loads after the splash screen.
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("TopicFlow - Home")
        self.setGeometry(300, 150, 600, 400)

        self.init_ui()

    def init_ui(self):
        # Welcome label
        self.label = QLabel("Welcome to TopicFlow", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Segoe UI", 16))
        self.label.setGeometry(150, 50, 300, 50)

        # Button to simulate starting a new project
        self.new_project_btn = QPushButton("Start New Project", self)
        self.new_project_btn.setGeometry(200, 150, 200, 40)

        # Button to simulate loading an existing project
        self.load_project_btn = QPushButton("Open Existing Project", self)
        self.load_project_btn.setGeometry(200, 210, 200, 40)

        # Settings button
        self.settings_btn = QPushButton("Settings", self)
        self.settings_btn.setGeometry(200, 270, 200, 40)
