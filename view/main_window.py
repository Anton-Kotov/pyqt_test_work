from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QTabWidget, QLabel

from view.pages.modeling_page import ModelingPage
from view.pages.prepare_data_page import PrepareDataPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(500, 500)
        title = "Тестовое задание"
        self.setWindowTitle(title)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)
        self.main_layout.setSpacing(10)
        self.main_layout.setContentsMargins(20, 20, 20, 20)

        self.tab_widget = QTabWidget()
        self.tab_widget.setTabPosition(QTabWidget.West)

        self.prepare_data_page = PrepareDataPage()
        self.modeling_page = ModelingPage()

        self.tab_widget.addTab(self.prepare_data_page, "Подготовка данных")
        self.tab_widget.addTab(self.modeling_page, "Моделирование")

        self.main_layout.addWidget(self.tab_widget)
