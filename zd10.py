import sqlite3


# Подключаемся к базе данных
def create_db():
    conn = sqlite3.connect('bus_station.db')
    cursor = conn.cursor()

    # Создаем таблицы
    cursor.execute('''CREATE TABLE IF NOT EXISTS stations (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS buses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        model TEXT NOT NULL,
                        license_plate TEXT NOT NULL,
                        capacity INTEGER NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS trips (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        station_id INTEGER,
                        bus_id INTEGER,
                        departure_time TEXT,
                        FOREIGN KEY(station_id) REFERENCES stations(id),
                        FOREIGN KEY(bus_id) REFERENCES buses(id))''')

    conn.commit()
    conn.close()


# Функция для добавления данных
def insert_data():
    conn = sqlite3.connect('bus_station.db')
    cursor = conn.cursor()

    # Добавляем станции
    cursor.executemany('''INSERT INTO stations (name) VALUES (?)''', [
        ('Station A',),
        ('Station B',)
    ])

    # Добавляем автобусы
    cursor.executemany('''INSERT INTO buses (model, license_plate, capacity) VALUES (?, ?, ?)''', [
        ('Bus Model X', '123ABC', 50),
        ('Bus Model Y', '456DEF', 60)
    ])

    # Добавляем рейсы
    cursor.executemany('''INSERT INTO trips (station_id, bus_id, departure_time) VALUES (?, ?, ?)''', [
        (1, 1, '08:00'),
        (1, 2, '09:00'),
        (2, 1, '10:00'),
        (2, 2, '11:00')
    ])

    conn.commit()
    conn.close()


# Функция для получения информации о рейсах и пассажирах
def get_trips_info():
    conn = sqlite3.connect('bus_station.db')
    cursor = conn.cursor()

    # Получаем информацию по станциям, количеству рейсов и пассажиров
    cursor.execute('''SELECT stations.name, COUNT(trips.id), SUM(buses.capacity)
                      FROM stations
                      LEFT JOIN trips ON stations.id = trips.station_id
                      LEFT JOIN buses ON buses.id = trips.bus_id
                      GROUP BY stations.id''')

    trips_info = cursor.fetchall()
    conn.close()

    return trips_info


# Функция для записи отчета в текстовый файл
def write_report_to_file(trips_info):
    with open("report.txt", "w") as file:
        file.write("Bus Station Report\n")
        file.write("----------------------\n")
        file.write(f"{'Station Name':<20} {'Number of Trips':<20} {'Total Passengers':<20}\n")
        file.write("----------------------\n")
        for station_name, num_trips, total_passengers in trips_info:
            file.write(f"{station_name:<20} {num_trips:<20} {total_passengers:<20}\n")


# Основная программа
def main():
    # Создаем базу данных и таблицы
    create_db()

    # Вставляем данные
    insert_data()

    # Получаем информацию о рейсах и пассажирах
    trips_info = get_trips_info()

    # Пишем отчет в текстовый файл
    write_report_to_file(trips_info)

    print("Report generated successfully. Check the 'report.txt' file.")


if __name__ == "__main__":
    main()
