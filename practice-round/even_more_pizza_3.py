# import numpy
# import math
from sys import argv
from collections import defaultdict


class Pizza:
    def __init__(self, id, size, ings):
        self.id = id
        self.size = size
        self.ings = ings


with open(argv[1], 'r') as f_in:
    num_pizzas, num_teams_2, num_teams_3, num_teams_4 = [
        int(n) for n in f_in.readline().split()]

    pizzas_by_size = []
    dict_ing = defaultdict(list)
    for id_pizza in range(num_pizzas):
        pizza_info = f_in.readline().split()
        pizza_size = pizza_info[0]
        pizza_ings = pizza_info[1:]
        for ingredient in pizza_ings:
            dict_ing[ingredient].append(id_pizza)
        pizzas_by_size.append(Pizza(id_pizza, pizza_size, pizza_ings))

    pizzas_by_size.sort(key=lambda pizza: pizza.size, reverse=True)

    candidate_ids = list(range(num_pizzas))

num_deliveries_4 = min(num_pizzas // 4, num_teams_4)
num_pizzas -= num_deliveries_4 * 4

num_deliveries_3 = min(num_pizzas // 3, num_teams_3)
num_pizzas -= num_deliveries_3 * 3

num_deliveries_2 = min(num_pizzas // 2, num_teams_2)

num_deliveries_total = num_deliveries_4 + num_deliveries_3 + num_deliveries_2


def pick_x_pizzas(x):
    first_pizza = pizzas_by_size[0]
    picked_ids = [first_pizza.id]
    picked_ings = [i for i in first_pizza.ings]
    max_unique = 0
    del pizzas_by_size[0]
    for i in range(2, x+1):
        for index in range(len(pizzas_by_size)):
            s = set(pizzas_by_size[index].ings) - set(picked_ings)
            if len(s) > max_unique:
                max_unique = len(s)
                max_index = index
                max_set = s
        picked_ings.append(n for n in max_set)
        picked_ids.append(pizzas_by_size[max_index].id)
        del pizzas_by_size[max_index]

    return picked_ids


with open(argv[1]+".out", 'w+') as f_out:
    deliveries = 0
    f_out.write(str(num_deliveries_total)+'\n')
    for i in range(num_deliveries_4):
        chosen_ids = pick_x_pizzas(4)
        f_out.write(" ".join(["4"] + [str(x) for x in chosen_ids] + ['\n']))
        deliveries += 4
        print(deliveries)
    for i in range(num_deliveries_3):
        chosen_ids = pick_x_pizzas(3)
        f_out.write(" ".join(["3"] + [str(x) for x in chosen_ids] + ['\n']))
        deliveries += 3
        print(deliveries)
    for i in range(num_deliveries_2):
        chosen_ids = pick_x_pizzas(2)
        f_out.write(" ".join(["2"] + [str(x) for x in chosen_ids] + ['\n']))
        deliveries += 2
        print(deliveries)
