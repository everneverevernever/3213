class Station:
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.trips = []  # Список рейсов, которые идут на эту станцию

    def add_trip(self, trip):
        self.trips.append(trip)


class Bus:
    def __init__(self, code, model, license_plate, capacity):
        self.code = code
        self.model = model
        self.license_plate = license_plate
        self.capacity = capacity


class Trip:
    def __init__(self, code, station, bus, departure_time):
        self.code = code
        self.station = station
        self.bus = bus
        self.departure_time = departure_time
        station.add_trip(self)  # Добавляем рейс на соответствующую станцию


def get_trips_info(stations):
    trips_info = []
    for station in stations:
        num_trips = len(station.trips)
        total_passengers = sum(trip.bus.capacity for trip in station.trips)
        trips_info.append((station.name, num_trips, total_passengers))
    return trips_info


def write_report_to_file(trips_info):
    with open("report.txt", "w") as file:
        file.write("Bus Station Report\n")
        file.write("----------------------\n")
        file.write(f"{'Station Name':<20} {'Number of Trips':<20} {'Total Passengers':<20}\n")
        file.write("----------------------\n")
        for station_name, num_trips, total_passengers in trips_info:
            file.write(f"{station_name:<20} {num_trips:<20} {total_passengers:<20}\n")


def main():
    # Инициализация автобусов
    bus1 = Bus(1, "Bus Model X", "123ABC", 50)
    bus2 = Bus(2, "Bus Model Y", "456DEF", 60)

    # Инициализация станций
    station1 = Station(1, "Station A")
    station2 = Station(2, "Station B")

    # Инициализация рейсов
    trip1 = Trip(1, station1, bus1, "08:00")
    trip2 = Trip(2, station1, bus2, "09:00")
    trip3 = Trip(3, station2, bus1, "10:00")
    trip4 = Trip(4, station2, bus2, "11:00")

    # Данные о станциях
    stations = [station1, station2]

    # Получаем информацию о рейсах и пассажирах
    trips_info = get_trips_info(stations)

    # Пишем отчет в текстовый файл
    write_report_to_file(trips_info)
    print("Report generated successfully. Check the 'report.txt' file.")


if __name__ == "__main__":
    main()
