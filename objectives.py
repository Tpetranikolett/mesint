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