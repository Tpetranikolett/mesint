import random
import copy

def mutate(s_of_routes, num_of_salesmen):
  mutant = copy.deepcopy(s_of_routes)
  a = random.randint(0, num_of_salesmen-1)
  b = random.randint(0, num_of_salesmen-1)
  ra = random.randint(1, len(mutant[a])-1)
  rb = random.randint(1, len(mutant[b])-1)
  if a == b:
    while ra == rb:
      rb = random.randint(1, len(mutant[b])-1)
  mutant[a][ra], mutant[b][rb] = mutant[b][rb], mutant[a][ra]
  return mutant

def crossover(parent_better, parent_worse, chunk_size, dict):
  if random.random() > (total_length(dict, parent_better))/(total_length(dict, parent_worse)):
    baby = copy.deepcopy(parent_better)
    better = 1
  else:
    baby = copy.deepcopy(parent_worse)
    better = 0
  a = [0] * chunk_size
  b = [0] * chunk_size
  for i in range(chunk_size):
    a[i] = random.randint(0, len(baby)-1)
  for j in range(chunk_size):
    b[j] = random.randint(1, len(baby[a[j]])-1)
  if better == 1:
    for k in range(chunk_size):
      sw = index_in_list(baby, parent_worse[a[k]][b[k]])
      baby[sw[0]][sw[1]], baby[a[k]][b[k]] = baby[a[k]][b[k]], baby[sw[0]][sw[1]]
  else:
    for k in range(chunk_size):
      sw = index_in_list(baby, parent_better[a[k]][b[k]])
      baby[sw[0]][sw[1]], baby[a[k]][b[k]] = baby[a[k]][b[k]], baby[sw[0]][sw[1]]
  return baby

def crossover_different(parent_better, parent_worse, dict):
  if random.random() > (total_length(dict, parent_better))/(total_length(dict, parent_worse)):
    baby = copy.deepcopy(parent_better)
    better = 1
  else:
    baby = copy.deepcopy(parent_worse)
    better = 0
  best = 0
  for i in range(len(baby)):
    if better == 1:
      best = 0
      shortest = length_of_route(dict, parent_worse[best])
      for j in range(len(parent_worse)):
        if length_of_route(dict, parent_worse[j]) < shortest:
          best = j
          shortest = length_of_route(dict, parent_worse[j])
      for k in range(len(baby[best])):
        sw = index_in_list(baby, parent_worse[best][k])
        baby[sw[0]][sw[1]], baby[best][k] = baby[best][k], baby[sw[0]][sw[1]]
    if better == 0:
      best = 0
      shortest = length_of_route(dict, parent_better[best])
      for j in range(len(parent_better)):
        if length_of_route(dict, parent_better[j]) < shortest:
          best = j
          shortest = length_of_route(dict, parent_better[j])
      for k in range(len(baby[best])):
        sw = index_in_list(baby, parent_better[best][k])
        baby[sw[0]][sw[1]], baby[best][k] = baby[best][k], baby[sw[0]][sw[1]]
  return baby

def genetic_alg(dict, s, population_size, generations, mutations, crossovers, num_of_salesmen):
  population = [list(s)]
  for _ in range(population_size - 1):
    population.append(mutate(s, num_of_salesmen))
  best_solution = max(population, key = lambda ch: total_length(dict, ch))
  shortest = total_length(dict, best_solution)
  for i in range(generations):
    for _ in range(mutations):
      population.append(mutate(population[random.randint(0, len(population) - 1)], num_of_salesmen))
    population = sorted(population, key = lambda ch: total_length(dict, ch))
    midpoint = int((len(population) - 1)/2)
    for _ in range(crossovers):
      worse = random.randint(midpoint, len(population)-1)
      better = random.randint(0, midpoint - 1)
      if random.random() > 0.5:
        population.append(crossover(population[better], population[worse], 3, dict))
      else:
        population.append(crossover_different(population[better], population[worse], dict))
    population = sorted(population, key=lambda ch: total_length(dict, ch))
    population = population[:population_size]
    best_chromosome = population[0]
    best_chromosome_route = total_length(dict, best_chromosome)
    if best_chromosome_route < shortest:
      shortest = best_chromosome_route
      best_solution = best_chromosome
      counter = 0
    else:
      counter += 1
    if counter == 15:
      print('generations: ', i)
      break
  return best_solution