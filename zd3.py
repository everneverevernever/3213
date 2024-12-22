import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QMessageBox

class BusStationApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Автовокзал")
        self.setGeometry(100, 100, 800, 600)

        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Код рейса", "Код станции", "Код автобуса", "Время отправления"])

        self.add_row_button = QPushButton("Добавить рейс", self)
        self.add_row_button.clicked.connect(self.add_row)

        self.delete_row_button = QPushButton("Удалить выбранный рейс", self)
        self.delete_row_button.clicked.connect(self.delete_selected_row)

        self.report_button = QPushButton("Сформировать отчет", self)
        self.report_button.clicked.connect(self.generate_report)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.add_row_button)
        layout.addWidget(self.delete_row_button)
        layout.addWidget(self.report_button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def add_row(self):
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

    def delete_selected_row(self):
        selected_row = self.table.currentRow()
        if selected_row != -1:
            self.table.removeRow(selected_row)

    def generate_report(self):
        try:
            station_report = {}

            for row in range(self.table.rowCount()):
                station_code = self.table.item(row, 1).text() if self.table.item(row, 1) else None

                if not station_code:
                    raise ValueError("Некорректные данные в таблице.")

                station_report[station_code] = station_report.get(station_code, 0) + 1

            report_message = "Отчет о рейсах:\n"
            for station, count in station_report.items():
                report_message += f"Станция {station}: {count} рейсов\n"

            with open("station_report.txt", "w", encoding="utf-8") as file:
                file.write(report_message)

            QMessageBox.information(self, "Отчет сформирован", "Отчет успешно записан в файл station_report.txt")
        except ValueError as e:
            QMessageBox.critical(self, "Ошибка", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Неизвестная ошибка", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BusStationApp()
    window.show()
    sys.exit(app.exec())
