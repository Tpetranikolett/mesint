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

  for i in range(len(h)):
    num_of_towns = h[i][0]
    num_of_salesmen = h[i][1]

    tsp = list()
    tsp = generate_towns(num_of_towns, tsp, 0, 1000)
    dict = transform_tsp(tsp)

    s = gen_starting_routes(num_of_towns, num_of_salesmen)
    divider()
    print('number of towns is: ', num_of_towns)
    print('number of salesmen is: ', num_of_salesmen, "\n")
    print('starting solution: ', s)
    print('total distance taken: ', total_length(dict, s), '\n')

    s_opt = genetic_alg(dict, s, 50, 50, 20, 20, num_of_salesmen, 10)
    print('optimal route is:', s_opt, '\ntotal distance taken: ', total_length(dict, s_opt))

  #showcasing my print_map
  """tsp2 = list()
  tsp2 = generate_towns(10, tsp2, 0, 30)
  print_map(tsp2, 30)"""

main()