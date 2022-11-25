import random

def distance (c1, c2):
  return ((c2[0] - c1[0])**2 + (c1[1] - c2[1])**2)**0.5

def generate_towns(num_of_towns, tsp, from_where, to_where):
  tsp = list()
  for i in range(num_of_towns):
    a = random.randint(from_where, to_where)
    b = random.randint(from_where, to_where)
    #print(a)
    #print(b)
    tsp.append((a, b))
    #print('location of town ', i, ' is: (', a ,',', b, ')') 
  return tsp

def transform_tsp(tsp):
  tsp_dict = {}
  for i in range(len(tsp)):
    for j in range(len(tsp)):
      tsp_dict[(i, j)] = distance(tsp[i], tsp[j])
  return tsp_dict

def length_of_route(dict, s): #s_of_route, tsp_dict
    dist = 0
    prev = s[0]
    for i in s:
        dist += dict[(prev, i)]
        prev = i
    dist += dict[(s[-1], s[0])]
    return dist

def total_length(dict, s):
  total_dist = 0
  for i in range(len(s)):
    dist = 0
    prev = s[i][0]
    for j in s[i]:
      dist += dict[(prev, j)]
      prev = j
    dist += dict[(s[i][-1], s[i][0])]
    total_dist = total_dist + dist
  return total_dist

def gen_starting_routes(num_of_towns, num_of_salesmen):
  s_of_routes = [[0, 0] for i in range(num_of_salesmen)]
  taken = []
  for i in range(num_of_salesmen):
    s_of_routes[i][0] = 0
  i = 0
  while i < (num_of_towns-1):
    current = random.randint(1, num_of_towns-1)
   # print('current number is: ', current)
   # print('i = ', i)
    if current not in taken:
      s_of_routes[i%num_of_salesmen].insert(-1, current)
    #  print('s_of_routes: ', i, ', s is: ', s_of_routes[i%num_of_salesmen], ' i%sm: ', i%num_of_salesmen)
      taken.append(current)
    #  print('taken: ', taken)
      i = i + 1
  """i = 0
  for i in range(num_of_salesmen):
    while len(s_of_routes[i]) < (num_of_towns-num_of_salesmen+1):
      s_of_routes[i].append(0)
    print('s_of_routes ', i, 'i s: ', s_of_routes[i])"""
  i = 0
  for i in range(num_of_salesmen):
    del s_of_routes[i][-1]
  return s_of_routes

def mutate(s_of_routes, num_of_salesmen):
  mutant = s_of_routes
  a = random.randint(0, num_of_salesmen-1)
  b = random.randint(0, num_of_salesmen-1)
  #print('a = ', a, ', b = ', b)
  ra = random.randint(1, len(mutant[a])-1)
  rb = random.randint(1, len(mutant[b])-1)
  if a == b:
    while ra == rb:
      rb = random.randint(1, len(mutant[b])-1)
      #print('ra = ', ra, ', rb = ', rb)
  mutant[a][ra], mutant[b][rb] = mutant[b][rb], mutant[a][ra]
  return mutant
  
def crossover(parent_better, parent_worse, chunk_size, num_of_sm, dict):
  #print("better parent is: ", parent_better)
  #print("worse_parent is: ", parent_worse)
  if random.random() > (total_length(dict, parent_better))/(total_length(dict, parent_worse)):
    baby = parent_better
    #print("baby is the better parent!")
  else:
    baby = parent_worse
    #print("baby is the worse parent!")
  a = [0] * chunk_size
  b = [0] * chunk_size
  #print(a, b)
  for i in range(chunk_size):
    a[i] = random.randint(0, num_of_sm-1)
    #print("ai is: ", a[i])
  for j in range(chunk_size):
    b[j] = random.randint(1, len(baby[a[j]])-1)
    #print("bi is: ", b[j])
  #print(a, b)
  if baby == parent_better:
    for k in range(chunk_size):
      #print("ak:", a[k], "bk: ", b[k])
      sw = index_in_list(baby, parent_worse[a[k]][b[k]])
      #print("number is: ", parent_worse[a[k]][b[k]])
      #print("sw0 is: ", sw[0])
      #print("sw1 is: ", sw[1])
      #print("ai is: ", a[k])
      #print("bi is: ", b[k])
      baby[sw[0]][sw[1]], baby[a[k]][b[k]] = baby[a[k]][b[k]], baby[sw[0]][sw[1]]
      #print("baby: swap1", baby[sw[0]][sw[1]],"baby swap2: " ,baby[a[k]][b[k]])
  else:
    for k in range(chunk_size):
      #print("ak:", a[k], "bk: ", b[k])
      sw = index_in_list(baby, parent_better[a[k]][b[k]])
      #print("number is: ", parent_better[a[k]][b[k]])
      #print("sw0 is: ", sw[0])
      #print("sw1 is: ", sw[1])
      #print("ai is: ", a[k])
      #print("bi is: ", b[k])
      baby[sw[0]][sw[1]], baby[a[k]][b[k]] = baby[a[k]][b[k]], baby[sw[0]][sw[1]]
      #print("baby: swap1", baby[sw[0]][sw[1]],"baby swap2: " ,baby[a[k]][b[k]])
  return baby

def genetic_alg(dict, s, population_size, generations, mutations, crossovers, num_of_salesmen):
  population = [list(s)]
  #population = [0] * population_size
  for _ in range(population_size - 1):
    population.append(mutate(s, num_of_salesmen))
  #best_solution = max(population, key = lambda ch: total_length(dict, ch))
  population = sorted(population, key = lambda ch: total_length(dict, ch))
  best_solution = population[0]
  #sort_solutions(population, dict)
  #best_solution = population[0]
  shortest = total_length(dict, best_solution)
  for _ in range(generations):
    for _ in range(mutations):
      population.append(mutate(population[random.randint(0, len(population) - 1)], num_of_salesmen))
    #print('--------------------')
    #print(*population, sep = '\n')
    population = sorted(population, key = lambda ch: total_length(dict, ch))
    #sort_solutions(population, dict)
    midpoint = int((len(population) - 1)/2)
    for _ in range(crossovers):
      worse = random.randint(midpoint, len(population)-1)
      better = random.randint(0, midpoint - 1)
      population.append(crossover(population[better], population[worse], 3, num_of_salesmen, dict))
    population = sorted(population, key=lambda ch: total_length(dict, ch))
    #print('------------------------------')
    #print('population after crossover: ', *population, sep = '\n')
    #sort_solutions(population, dict)
    population = population[:population_size]
    best_chromosome = population[0]
    best_chromosome_route = total_length(dict, best_chromosome)
    if best_chromosome_route < shortest:
      shortest = best_chromosome_route
      best_solution = best_chromosome
  return best_solution


def sort_solutions(s_of_solutions, dict):
  for i in range(len(s_of_solutions)):
    min = i
    #min_value = total_length(dict, s_of_solutions[i])
    for j in range((i+1), len(s_of_solutions)):
      if total_length(dict, s_of_solutions[j]) < total_length(dict, s_of_solutions[min]):
        min = j
    if(s_of_solutions[i] != s_of_solutions[min]):
      s_of_solutions[i], s_of_solutions[min] = s_of_solutions[min], s_of_solutions[i]
  return s_of_solutions
  
    
  
def index_in_list(list_of_lists, value):
  a = list()
  a = [0] * 2
  for i, lst in enumerate(list_of_lists):
    if value in lst:
      a[0] = i
      a[1] = lst.index(value)
      break
  return a


        

      
def main():
  num_of_towns = 10
  num_of_salesmen = 3
  tsp = list()
  tsp = generate_towns(num_of_towns, tsp, 0, 1000)
  dict = transform_tsp(tsp)
  #s_of_solutions = list()
  #s_of_solutions = [0] * 10
  s = gen_starting_routes(num_of_towns, num_of_salesmen)
  print(s)
  print('total distance of the routes: ', total_length(dict, s))
  #s_opt = genetic_alg(dict, s, 10, 10, 5, 5, num_of_salesmen)
  #print(s_opt, total_length(dict, s_opt))

  lista = list()
  for i in range(5):
    lista.append(mutate(s, num_of_salesmen))
    print(lista[i])

  print('----------')
  print(*lista, sep = '\n')
  print('-----------')
  print(s)

main()