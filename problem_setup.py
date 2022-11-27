import random

def define_starting_data():
  towns = [10, 20, 50, 100, 200, 500]
  salesmen_small = [1, 2, 4, 5]
  salesmen_big = [10, 20]
  starting_data = list()
  for i in range(len(towns)):
    num_of_towns = towns[i]
    if towns[i] > 49:
      for j in range(len(salesmen_big)):
        num_of_salesmen = salesmen_big[j]
        starting_data.append([num_of_towns, num_of_salesmen])
    elif towns[i] == 10:
      for j in range(len(salesmen_small)-1):
        num_of_salesmen = salesmen_small[j]
        starting_data.append([num_of_towns, num_of_salesmen])
    else:
      for j in range(len(salesmen_small)):
        num_of_salesmen = salesmen_small[j]
        starting_data.append([num_of_towns, num_of_salesmen])
  return starting_data 

def gen_starting_routes(num_of_towns, num_of_salesmen):
  s_of_routes = [[0, 0] for _ in range(num_of_salesmen)]
  taken = []
  for i in range(num_of_salesmen):
    s_of_routes[i][0] = 0
  i = 0
  while i < (num_of_towns-1):
    current = random.randint(1, num_of_towns-1)
    if current not in taken:
      s_of_routes[i%num_of_salesmen].insert(-1, current)
      taken.append(current)
      i = i + 1
  i = 0
  for i in range(num_of_salesmen):
    del s_of_routes[i][-1]
  return s_of_routes