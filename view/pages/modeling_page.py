from PyQt5.QtWidgets import QTableView, QTabWidget, QVBoxLayout

from test.view.pages.model_dev_page import ModelDevPage
from test.view.pages.parameters_page import ParametersPage


class ModelingPage(QTableView):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setSpacing(10)
        self.main_layout.setContentsMargins(10, 10, 10, 10)

        self.tab_widget = QTabWidget()
        self.parameters_page = ParametersPage()
        self.model_dev_page = ModelDevPage()

        self.tab_widget.addTab(self.parameters_page, "Параметры")
        self.tab_widget.addTab(self.model_dev_page, "Разработка моделей")

        self.main_layout.addWidget(self.tab_widget)
