def index_in_list(list_of_lists, value):
  a = list()
  a = [0] * 2
  for i, lst in enumerate(list_of_lists):
    if value in lst:
      a[0] = i
      a[1] = lst.index(value)
      break
  return a

def print_map(tsp, to_p):
  for i in range(to_p):
    for j in range(to_p):
      if j < to_p-1:
        if (i,j) in tsp:
          print("o ", end='')
        if(i,j) not in tsp:
          print('  ', end='')
      if j == to_p-1:
        if (i, j) in tsp:
          print("o")
        if (i,j) not in tsp:
          print(" ")