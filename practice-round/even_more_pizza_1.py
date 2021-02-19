# import numpy
# import math
from sys import argv


class Pizza:
  def __init__(self, id, size):
    self.id = id
    self.size = size


with open(argv[1], 'r') as f_in:
  first_line = f_in.readline()
  num_pizzas, num_teams_2, num_teams_3, num_teams_4 = [
      int(n) for n in first_line.split()]

  list_pizzas = []
  for id_pizza in range(num_pizzas):
    pizza_size = f_in.readline().split()[0]
    list_pizzas.append(Pizza(id_pizza, pizza_size))

list_pizzas.sort(key=lambda pizza: pizza.size, reverse=True)


num_deliveries_4 = min(num_pizzas // 4, num_teams_4)
num_pizzas -= num_deliveries_4 * 4

num_deliveries_3 = min(num_pizzas // 3, num_teams_3)
num_pizzas -= num_deliveries_3 * 3

num_deliveries_2 = min(num_pizzas // 2, num_teams_2)

num_deliveries_total = num_deliveries_4 + num_deliveries_3 + num_deliveries_2

with open(argv[1]+".out", 'w+') as f_out:
  f_out.write(str(num_deliveries_total)+'\n')
  for i in range(num_deliveries_4):
    chosen_ids = []
    for j in range(4):
      chosen_ids.append(list_pizzas[0].id)
      del list_pizzas[0]
    f_out.write(" ".join(["4"] + [str(x) for x in chosen_ids] + ['\n']))
  for i in range(num_deliveries_3):
    chosen_ids = []
    for j in range(3):
      chosen_ids.append(list_pizzas[0].id)
      del list_pizzas[0]
    f_out.write(" ".join(["3"] + [str(x) for x in chosen_ids] + ['\n']))
  for i in range(num_deliveries_2):
    chosen_ids = []
    for j in range(2):
      chosen_ids.append(list_pizzas[0].id)
      del list_pizzas[0]
    f_out.write(" ".join(["2"] + [str(x) for x in chosen_ids] + ['\n']))
