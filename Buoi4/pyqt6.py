import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Giao Diện Đơn Giản PyQt6")
        self.setGeometry(100, 100, 400, 300)

        # Tạo layout chính
        layout = QVBoxLayout()

        # Tạo nhãn
        self.label = QLabel("Chào mừng bạn đến với PyQt6!", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Canh giữa nội dung
        self.label.setStyleSheet("font-size: 16px; color: blue;")
        layout.addWidget(self.label)

        # Tạo nút bấm
        self.button = QPushButton("Nhấn vào đây", self)
        self.button.clicked.connect(self.on_button_click)
        layout.addWidget(self.button)

        # Thiết lập widget chính
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def on_button_click(self):
        self.label.setText("Bạn đã nhấn nút!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
