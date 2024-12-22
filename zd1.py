import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QFileDialog
from openpyxl import Workbook

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

        self.save_button = QPushButton("Сохранить в Excel", self)
        self.save_button.clicked.connect(self.save_to_excel)

        self.calculate_button = QPushButton("Рассчитать данные", self)
        self.calculate_button.clicked.connect(self.calculate_data)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.add_row_button)
        layout.addWidget(self.delete_row_button)
        layout.addWidget(self.save_button)
        layout.addWidget(self.calculate_button)

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

    def save_to_excel(self):
        path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Excel Files (*.xlsx)")
        if path:
            workbook = Workbook()
            sheet = workbook.active

            # Write headers
            headers = [self.table.horizontalHeaderItem(col).text() for col in range(self.table.columnCount())]
            sheet.append(headers)

            # Write table content
            for row in range(self.table.rowCount()):
                row_data = []
                for col in range(self.table.columnCount()):
                    item = self.table.item(row, col)
                    row_data.append(item.text() if item else "")
                sheet.append(row_data)

            workbook.save(path)

    def calculate_data(self):
        station_count = {}
        total_capacity = 0

        for row in range(self.table.rowCount()):
            station_code = self.table.item(row, 1).text() if self.table.item(row, 1) else None
            bus_code = self.table.item(row, 2).text() if self.table.item(row, 2) else None

            if station_code:
                station_count[station_code] = station_count.get(station_code, 0) + 1

            if bus_code:
                # Здесь нужно получить вместимость автобуса по коду (пример - 50 пассажиров на автобус)
                total_capacity += 50  # В реальной программе данные берутся из базы или списка

        print("Рейсы до каждой станции:")
        for station, count in station_count.items():
            print(f"Станция {station}: {count} рейсов")

        print(f"Общее количество пассажиров: {total_capacity}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BusStationApp()
    window.show()
    sys.exit(app.exec())
