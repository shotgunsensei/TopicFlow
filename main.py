import sys
from PyQt5.QtWidgets import QApplication
from ui.splash import SplashScreen

if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()
    sys.exit(app.exec_())