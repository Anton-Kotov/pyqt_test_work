from PyQt5.QtWidgets import QFrame, QVBoxLayout, QSizePolicy


class BaseWidget(QFrame):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout(self)
        self.setStyleSheet("""BaseWidget {
            border: 8px solid #f0f0f0;
            border-radius: 10px;
            background-color: #FFFFFF;
            }"""
        )