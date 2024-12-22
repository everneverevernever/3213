import sqlite3
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem


# 1. Классы для работы с данными

class Station:
    def __init__(self, code, name):
        self.code = code
        self.name = name


class Bus:
    def __init__(self, code, model, license_plate, capacity):
        self.code = code
        self.model = model
        self.license_plate = license_plate
        self.capacity = capacity


class Trip:
    def __init__(self, code, station_code, bus_code, departure_time):
        self.code = code
        self.station_code = station_code
        self.bus_code = bus_code
        self.departure_time = departure_time


# 2. Работа с базой данных

def create_database():
    conn = sqlite3.connect("bus_station.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stations (
        code INTEGER PRIMARY KEY,
        name TEXT
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS buses (
        code INTEGER PRIMARY KEY,
        model TEXT,
        license_plate TEXT,
        capacity INTEGER
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trips (
        code INTEGER PRIMARY KEY,
        station_code INTEGER,
        bus_code INTEGER,
        departure_time TEXT,
        FOREIGN KEY (station_code) REFERENCES stations(code),
        FOREIGN KEY (bus_code) REFERENCES buses(code)
    )""")
    conn.commit()
    conn.close()


def add_sample_data():
    conn = sqlite3.connect("bus_station.db")
    cursor = conn.cursor()

    # Добавление станций
    cursor.execute("INSERT INTO stations (code, name) VALUES (1, 'Station A')")
    cursor.execute("INSERT INTO stations (code, name) VALUES (2, 'Station B')")

    # Добавление автобусов
    cursor.execute("INSERT INTO buses (code, model, license_plate, capacity) VALUES (1, 'Bus Model X', '123ABC', 50)")
    cursor.execute("INSERT INTO buses (code, model, license_plate, capacity) VALUES (2, 'Bus Model Y', '456DEF', 60)")

    # Добавление рейсов
    cursor.execute("INSERT INTO trips (code, station_code, bus_code, departure_time) VALUES (1, 1, 1, '08:00')")
    cursor.execute("INSERT INTO trips (code, station_code, bus_code, departure_time) VALUES (2, 1, 2, '09:00')")
    cursor.execute("INSERT INTO trips (code, station_code, bus_code, departure_time) VALUES (3, 2, 1, '10:00')")
    cursor.execute("INSERT INTO trips (code, station_code, bus_code, departure_time) VALUES (4, 2, 2, '11:00')")

    conn.commit()
    conn.close()


# 3. Логика для подсчета рейсов и пассажиров

def get_trips_info():
    conn = sqlite3.connect("bus_station.db")
    cursor = conn.cursor()

    query = """
    SELECT s.name, COUNT(t.code) AS num_trips, SUM(b.capacity) AS total_passengers
    FROM stations s
    LEFT JOIN trips t ON s.code = t.station_code
    LEFT JOIN buses b ON t.bus_code = b.code
    GROUP BY s.code
    """
    cursor.execute(query)
    trips_info = cursor.fetchall()
    conn.close()

    return trips_info


# 4. Интерфейс с PyQt6

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bus Station Information")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.table = QTableWidget(self)
        layout.addWidget(self.table)

        self.load_data_button = QPushButton("Load Data", self)
        layout.addWidget(self.load_data_button)
        self.load_data_button.clicked.connect(self.load_data)

        self.setLayout(layout)

    def load_data(self):
        trips_info = get_trips_info()

        self.table.setRowCount(len(trips_info))
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Station Name", "Number of Trips", "Total Passengers"])

        for row, (station_name, num_trips, total_passengers) in enumerate(trips_info):
            self.table.setItem(row, 0, QTableWidgetItem(station_name))
            self.table.setItem(row, 1, QTableWidgetItem(str(num_trips)))
            self.table.setItem(row, 2, QTableWidgetItem(str(total_passengers)))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    create_database()
    add_sample_data()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
