from view.base_cls import BaseWidget
import pyqtgraph as pg


class GraphWidget(BaseWidget):
    def __init__(self):
        super().__init__()
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBackground('white')
        self.main_layout.addWidget(self.plot_widget)
