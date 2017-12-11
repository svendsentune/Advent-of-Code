from math import sqrt,floor,ceil
from itertools import permutations

"""
http://adventofcode.com/2017/day/3
"""

class Spiral:
    """
    A simple example class
    Maybe create attribute "reverse"
    """
    def __init__(self,k):
      self.start_i = 0
      self.start_j = 0
      self.shape = [[0 for j in range(1,k+1)] for i in range(0,k)]
      self.starting_direction = "right"
      self.length = k
      self.cycle = {"right":"down","down":"left","left":"up","up":"right"}
      self.direction = ""
      self.path = []

    def create(self):

      self.shape[0][0] = self.length**2
      numbers = list(reversed(range(1,self.length**2)))
      self.direction = self.starting_direction
      i = self.start_i
      j = self.start_j
      number = numbers[0]
      self.path.append((i,j))
      while number >= numbers[-1]:
        self.shape,i,j = self.walk(i,j,self.direction,self.shape,number)
        self.path.append((i,j))
        number-=1
      return self.shape

    def walk(self,row,col,direction,shape,number):
      if direction == "right":
        try:
          if shape[row][col+1] == 0:
            shape[row][col+1] = number
            return shape,row,col+1
          else:
            self.direction = "down"
            return self.walk(row,col,self.direction,shape,number)
        except IndexError:
          self.direction = "down"
          return self.walk(row,col,self.direction,shape,number)
      elif direction == "down":
        try:
          if shape[row+1][col] == 0:
            shape[row+1][col] = number
            return shape,row+1,col
          else:
            self.direction = "left"
            return self.walk(row,col,self.direction,shape,number)
        except IndexError:
          self.direction = "left"
          return self.walk(row,col,self.direction,shape,number)
      elif direction == "left":
        try:
          if shape[row-1][col] == 0:
            shape[row-1][col] = number
            return shape,row-1,col
          else:
            self.direction = "up"
            return self.walk(row,col,self.direction,shape,number)
        except IndexError:
          self.direction = "up"
          return self.walk(row,col,self.direction,shape,number)
      else:
        try:
          if shape[row][col-1] == 0:
            shape[row][col-1] = number
            return shape,row,col-1
          else:
            self.direction = "right"
            return self.walk(row,col,self.direction,shape,number)
        except IndexError:
          self.direction = "right"
          return self.walk(row,col,self.direction,shape,number)




def spiralGrid(n):
  spiral = Spiral(n)
  spiral.create()
  return spiral.shape

def getMax(integer):
  if ceil(sqrt(integer)) % 2 != 0:
    return ceil(sqrt(integer))
  else:
    return (ceil(sqrt(integer))+1)

def spiralMemory(integer):
  grid = spiralGrid(getMax(integer))
  start_pos = (int(floor(len(grid)/2)),int(floor(len(grid)/2)))
  for i,r in enumerate(grid):
    for j,c in enumerate(r):
      if c == integer:
        return abs(start_pos[0]-i)+abs(start_pos[1]-j)


def getSumAdjacent(pos,dic,neighbors):
  c = 0
  for n in neighbors:
    try:
      c+=dic[(pos[0]+n[0],pos[1]+n[1])]
    except KeyError:
      continue
  return c


def spiralAdjacent(integer):
  spiral = Spiral(getMax(integer))
  spiral.create()
  path = list(reversed(spiral.path))
  neighbors = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
  spiral_dict = {path[0]:1}
  result = 1
  for p in path[1:]:
    result = getSumAdjacent(p,spiral_dict,neighbors)
    if result > integer:
      break
    spiral_dict[p] = getSumAdjacent(p,spiral_dict,neighbors)
  return result



#print(spiralMemory(265149))

print(spiralAdjacent(265149))
