import random
from addons import *
from genetic import *
from objectives import *
from problem_setup import *
from tsp import *

def main():
  random.seed(100)
  h = define_starting_data()
  print(h)
  num_of_towns = h[0]
  num_of_salesmen = h[1]

  tsp = list()
  tsp = generate_towns(num_of_towns, tsp, 0, 1000)
  dict = transform_tsp(tsp)

  s = gen_starting_routes(num_of_towns, num_of_salesmen)
  print('starting solution: ', s)
  print('total distance taken: ', total_length(dict, s))
  
  s_opt = genetic_alg(dict, s, 50, 50, 20, 20, num_of_salesmen)
  print('optimal route is:', s_opt, '\ntotal distance taken: ', total_length(dict, s_opt))

  #showcasing my print_map in a smaller version
  tsp2 = list()
  tsp2 = generate_towns(10, tsp2, 0, 30)
  print_map(tsp2, 30)

main()