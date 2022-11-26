import random

def distance (c1, c2):
  return ((c2[0] - c1[0])**2 + (c1[1] - c2[1])**2)**0.5


def transform_tsp(tsp):
  tsp_dict = {}
  for i in range(len(tsp)):
    for j in range(len(tsp)):
      tsp_dict[(i, j)] = distance(tsp[i], tsp[j])
  return tsp_dict

def generate_towns(num_of_towns, tsp, from_where, to_where):
  tsp = list()
  for i in range(num_of_towns):
    a = random.randint(from_where, to_where)
    b = random.randint(from_where, to_where)
    tsp.append((a, b))
  return tsp
