from collections import Counter

"""
http://adventofcode.com/2017/day/6
"""

def memoryAllocation(t):
  l = [int(i) for i in t.split("\t")]
  #l = [0,2,7,0]
  states = Counter()
  states[i2s(l)] = 1
  cycle = 0
  done = False
  print(states)
  while done == False:
    most_index,most_value = getMaxIndex(l)
    l[most_index] = 0
    current_index = most_index+1
    while most_value > 0:
      try:
        l[current_index] += 1
        current_index += 1
        most_value -= 1
      except IndexError:
        current_index = 0
    cycle+=1
    if states[i2s(l)] == 2:
      done = True
      print('yoooo',states)
    else:
      states[i2s(l)]+=1
  return cycle

def getMaxIndex(lst):
  most = max(lst)
  for i,v in enumerate(lst):
    if v == most:
      return i,v

def i2s(integerlist):
  return "".join(str(i) for i in integerlist)

print(memoryAllocation("""11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11"""))
