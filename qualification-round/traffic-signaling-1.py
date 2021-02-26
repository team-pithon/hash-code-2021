from sys import argv


class Intersection:
    def __init__(self, id):
        self.id = id
        self.ins = []
        self.num_ins = 0

    def add_in(self, new):
        self.ins.append(new)
        self.num_ins += 1


with open(argv[1], 'r') as f_in:
    sim_dur, num_intersec, num_streets, num_cars, bonus = [
        int(n) for n in f_in.readline().split()]

    list_intersec = []
    for i in range(num_intersec):
        list_intersec.append(Intersection(i))

    for i in range(num_streets):
        line = f_in.readline().split(" ")
        list_intersec[int(line[1])].add_in(line[2])


with open(argv[1].split('.')[0]+".out", 'w+') as f_out:
    f_out.write(str(num_intersec)+'\n')
    for intersec in list_intersec:
        f_out.write(str(intersec.id) + '\n' + str(intersec.num_ins) + '\n')
        for in_street in intersec.ins:
            f_out.write(str(in_street) + ' 1\n')
