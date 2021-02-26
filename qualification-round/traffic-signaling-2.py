from sys import argv


class Intersection:
    def __init__(self, id):
        self.id = id
        self.ins = []
        self.num_ins = 0

    def add_in(self, new):
        self.ins.append(new)
        self.num_ins += 1

    def sort(self, dic):
        self.ins.sort(key=lambda street: dic[street], reverse=True)


with open(argv[1], 'r') as f_in:
    sim_dur, num_intersec, num_streets, num_cars, bonus = [
        int(n) for n in f_in.readline().split()]

    list_intersec = []
    for i in range(num_intersec):
        list_intersec.append(Intersection(i))

    street_times = {}

    for i in range(num_streets):
        line = f_in.readline().split(" ")
        list_intersec[int(line[1])].add_in(line[2])
        street_times[line[2]] = 0

    for i in range(num_cars):
        line = f_in.readline().split(" ")
        del line[0]
        line[-1] = line[-1][:-1]
        for street_name in line:
            street_times[street_name] += 1


with open(argv[1].split('.')[0]+".out", 'w+') as f_out:
    f_out.write(str(num_intersec)+'\n')
    for intersec in list_intersec:
        f_out.write(str(intersec.id) + '\n' + str(intersec.num_ins) + '\n')

        # trivial
        if intersec.num_ins == 1:
            f_out.write(str(intersec.ins[0]) + ' 1\n')

        # change!
        else:
            intersec.sort(street_times)
            for i in range(intersec.num_ins):
                f_out.write(str(intersec.ins[i]) + ' ' +
                            str(intersec.num_ins - i) + '\n')
