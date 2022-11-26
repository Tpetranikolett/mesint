import random

def define_starting_data():
  towns = [10, 20, 50, 100, 200, 500]
  salesmen_small = [1, 2, 4, 5]
  salesmen_big = [10, 20]
  num_of_towns = random.choice(towns)
  if num_of_towns > 49:
    num_of_salesmen = random.choice(salesmen_big)
  else:
    num_of_salesmen = random.choice(salesmen_small)
  starting_data = [num_of_towns, num_of_salesmen]
  return starting_data 

def gen_starting_routes(num_of_towns, num_of_salesmen):
  s_of_routes = [[0, 0] for i in range(num_of_salesmen)]
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