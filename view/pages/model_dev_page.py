from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableView, QGridLayout, QLabel, QSizePolicy

from view.factors_list_widget import FactorsListWidget
from view.graph_widget import GraphWidget


class ModelDevPage(QTableView):
    def __init__(self):
        super().__init__()
        self.main_layout = QGridLayout(self)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(5)
        self.main_layout.setAlignment(Qt.AlignTop)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.factors_list_title = QLabel("Список факторов")
        self.graph_title = QLabel("График")

        self.main_layout.addWidget(self.factors_list_title, 0, 0)
        self.main_layout.addWidget(self.graph_title, 0, 1)

        self.graph_widget = GraphWidget()
        self.factors_list_widget = FactorsListWidget(self)

        self.main_layout.addWidget(self.factors_list_widget, 1, 0)
        self.main_layout.addWidget(self.graph_widget, 1, 1)
