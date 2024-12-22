import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget
import random

class RandomDataApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Демонстрация случайных данных")
        self.setGeometry(100, 100, 600, 400)

        self.label = QLabel("Нажмите кнопку для генерации данных", self)
        self.label.setStyleSheet("font-size: 16px;")

        self.generate_button = QPushButton("Сгенерировать данные", self)
        self.generate_button.clicked.connect(self.generate_random_data)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.generate_button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def generate_random_data(self):
        try:
            num_stations = random.randint(3, 10)
            stations = {f"Станция {i+1}": random.randint(1, 20) for i in range(num_stations)}

            report_message = "Случайные данные о рейсах:\n"
            for station, count in stations.items():
                report_message += f"{station}: {count} рейсов\n"

            self.label.setText(report_message)
        except Exception as e:
            self.label.setText(f"Ошибка: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RandomDataApp()
    window.show()
    sys.exit(app.exec())
