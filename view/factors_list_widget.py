from __future__ import annotations

from functools import partial
from random import randint
from typing import TYPE_CHECKING

from PyQt5.QtWidgets import QCheckBox

from control.graph_random_data import GraphRandomData
from view.base_cls import BaseWidget

if TYPE_CHECKING:
    from view.pages.model_dev_page import ModelDevPage


class FactorsListWidget(BaseWidget):
    def __init__(self, model_dev_page: ModelDevPage):
        super().__init__()
        self.plot_widget = model_dev_page.graph_widget.plot_widget
        self.setMinimumHeight(300)
        self.add_checkbox()
        self.main_layout.addStretch(1)

    def add_checkbox(self):
        for i in range(1, 11):
            color = f"#{randint(0, 0xFFFFFF):06x}"

            check_box = QCheckBox()
            check_box.setText(f"Параметр {i}")
            check_box.setStyleSheet(f"color: {color};")

            graph_data = next(GraphRandomData())
            plot = self.plot_widget.plot(
                graph_data.x_pos,
                graph_data.y_pos,
                pen=color,
                name=f"График {i}"
            )
            plot.hide()

            check_box.stateChanged.connect(partial(self.checkbox_clicked, plot))
            self.main_layout.addWidget(check_box)

    def checkbox_clicked(self, plot, check_state: int):
        plot.show() if check_state else plot.hide()

