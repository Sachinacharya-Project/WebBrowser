import sys
from PyQt5 import QtGui, QtCore, QtWidgets, QtWebEngineWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QtWebEngineWidgets.QWebEngineView()
        self.browser.setUrl(QtCore.QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        self.setWindowIcon(QtGui.QIcon('mybrowserIcon.png'))
        nav_stylesheet = """
        background-color: #444;
        color: white;
        height: 20px;
        padding: 5px;
        font-weight: bold;
        font-family: sans-serif;
        border: none;
        """
        url_stylesheet = """
            outline: none;
            border: 1px solid white;
        """
        # navbar
        navbar = QtWidgets.QToolBar()
        self.addToolBar(navbar)
        navbar.setStyleSheet(nav_stylesheet)
        navbar.setMovable(False)
        # navbar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape('pointer'))
        back_btn = QtWidgets.QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QtWidgets.QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QtWidgets.QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QtWidgets.QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QtWidgets.QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.url_bar.setStyleSheet(url_stylesheet)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QtCore.QUrl('https://www.sachinacharya.cf'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QtCore.QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QtWidgets.QApplication(sys.argv)
QtWidgets.QApplication.setApplicationName('MyBrowser')
window = MainWindow()
app.exec_()