from sys import argv


class Intersection:
    def __init__(self, id):
        self.id = id
        self.ins = {}
        self.num_ins = 0
        self.history = {}

    def add_in(self, street):
        self.ins[street] = []
        self.num_ins += 1
        self.history[street] = 1

    def add_car(self, origin_street, car):
        self.ins[origin_street].append(car)

    def turn_on_semaphore(self, street_in):
        self.history[street_in] += 1


class Street:
    def __init__(self, intersec, len):
        self.intersec = intersec
        self.len = len


class Car:
    def __init__(self, id, time_to_next_intersec, curr_street, route):
        self.id = id
        self.time_to_next_intersec = time_to_next_intersec
        self.curr_street = curr_street
        self.route = route  # lista com nomes das ruas


# tratar input
with open(argv[1], 'r') as f_in:
    sim_dur, num_intersec, num_streets, num_cars, bonus = [
        int(n) for n in f_in.readline().split()]

    list_intersec = []
    for i in range(num_intersec):
        list_intersec.append(Intersection(i))

    streets = {}
    for i in range(num_streets):
        line = f_in.readline().split(" ")
        list_intersec[int(line[1])].add_in(line[2])
        streets[line[2]] = Street(list_intersec[int(line[1])], int(line[3]))

    for i in range(num_cars):
        line = f_in.readline().split(" ")
        line[-1] = line[-1][:-1]
        del line[0]
        start_street = line[0]
        car = Car(i, 0, start_street, [street for street in line])
        intersec = streets[start_street].intersec
        list_intersec[intersec.id].add_car(start_street, car)

        # escrever o out
with open(argv[1].split('.')[0]+".out", 'w+') as f_out:

    f_out.write(str(num_intersec)+'\n')

    travelling_cars = []

    for instant in range(sim_dur):

        # tratar carros em viagem
        for car in travelling_cars:
            car.time_to_next_intersec -= 1
            if car.time_to_next_intersec == 0:
                streets[car.curr_street].intersec.add_car(car.curr_street, car)
        travelling_cars = [
            car for car in travelling_cars if not car.time_to_next_intersec == 0]

        # determinar dados os percursos q semaforos compativeis ligar
        for intersec in list_intersec:
            v = [len(x) for x in list(intersec.ins.values())]
            k = list(intersec.ins.keys())

            selected_street = k[v.index(max(v))]
            if intersec.ins[selected_street]:
                intersec.turn_on_semaphore(selected_street)
                car = intersec.ins[selected_street][0]
                intersec.ins[selected_street] = intersec.ins[selected_street][1:]
                car.route.pop()
                if len(car.route) > 1:  # nao chegou ao destino
                    car.curr_street = car.route[0]
                    car.time_to_next_intersec = streets[car.curr_street].len
                    travelling_cars.append(car)

    for intersec in list_intersec:
        # trivial
        if intersec.num_ins == 1:
            f_out.write(str(intersec.id) + '\n1\n' +
                        str(list(intersec.ins.keys())[0]) + ' 1\n')

        # change!
        else:
            f_out.write(str(intersec.id) + '\n' +
                        str(len(intersec.history)) + '\n')
            for k, v in intersec.history.items():
                f_out.write(str(k) + ' ' + str(v) + '\n')
