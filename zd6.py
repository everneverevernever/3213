import sys
import json
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget

class ReportApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Демонстрация системы классов")
        self.setGeometry(100, 100, 600, 400)

        self.label = QLabel("Сформируйте отчет", self)
        self.label.setStyleSheet("font-size: 16px;")

        self.generate_report_button = QPushButton("Сформировать отчет", self)
        self.generate_report_button.clicked.connect(self.generate_report)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.generate_report_button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def generate_report(self):
        try:
            stations = {
                "Станция 1": 5,
                "Станция 2": 3,
                "Станция 3": 7
            }

            report = "Отчет о рейсах:\n"
            for station, trips in stations.items():
                report += f"{station}: {trips} рейсов\n"

            self.label.setText(report)

            with open("report.txt", "w", encoding="utf-8") as file:
                file.write(report)
        except Exception as e:
            self.label.setText(f"Ошибка: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReportApp()
    window.show()
    sys.exit(app.exec())
