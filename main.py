


class Race:
    def __init__(self):
        self.code_race = []
        self.code_station = []
        self.code_bus = []
        self.code_starts = []

    def read_file(self):
        with open('races.txt', 'r', encoding='utf-8') as file:
            for line in file:
                code_race, code_station, code_bus, code_starts = line.split()
                self.code_race.append(code_race)
                self.code_station.append(code_station)
                self.code_bus.append(code_bus)
                self.code_starts.append(code_starts)

    def get_race_and_station(self, station):
        itog = {}
        for code_race, code_station in zip(self.code_race, self.code_station):
            itog[code_race] = code_station

        return itog

    def get_kolvo_race_name_station(self, station):
        itog = self.get_race_and_station(station)
        itog_station = {}
        for id in itog:
            data = itog.get(id)
            sum = 1
            if data in station.code_station:
                index = station.code_station.index(data)
                itog_station = {station.name_station[index]: 1}
                if station.name_station[index] in itog_station:
                    itog_station[station.name_station[index]] += 1

        return itog_station

class Station:
    def __init__(self):
        self.code_station = []
        self.name_station = []

    def read_file(self):
        with open('station.txt', 'r', encoding='utf-8') as file:
            for line in file:
                code_station, name_station = line.split()
                self.code_station.append(code_station)
                self.name_station.append(name_station)

class Bus:
    def __init__(self):
        self.code_bus = []
        self.mark_bus= []
        self.gos_number = []
        self.capacity = []

    def read_file(self):
        with open('bus.txt', 'r', encoding='utf-8') as file:
            for line in file:
                code_bus, mark_bus, gos_number, capacity = line.split()
                self.code_bus.append(code_bus)
                self.mark_bus.append(mark_bus)
                self.gos_number.append(gos_number)
                self.capacity.append(capacity)

    def sum_bus_capacity(self):
        sum = 0
        for capacity_bus in self.capacity:
            sum += int(capacity_bus)
        return sum

def main():
    race = Race()
    race.read_file()
    station = Station()
    station.read_file()
    bus = Bus()
    bus.read_file()

    print(f'Итоговая вместительность всех пассажиров во все автобусы: {bus.sum_bus_capacity()}')
    print(f'Итоговое кол-во рейсов до каждой станции: {race.get_kolvo_race_name_station(station)}')


main()