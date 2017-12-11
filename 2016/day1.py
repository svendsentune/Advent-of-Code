"""
https://adventofcode.com/2016/day/2
"""


r_dict = {"north":"east","east":"south","south":"west","west":"north"}

l_dict = {"north":"west","west":"south","south":"east","east":"north"}

def walkingAbout(text_directions):
  directions = text_directions.split(", ")
  pos = [0,0]
  face = "north"
  all_pos = [[0,0]]
  for d in directions:
    turn = d[0]
    distance = int(d[1:])
    if turn == "L":
      face = l_dict[face]
    else:
      face = r_dict[face]
    if face == "north":
      old_pos = pos[:]
      pos[1]+=distance
      new_pos = pos
    elif face == "east":
      old_pos = pos[:]
      pos[0]+=distance
      new_pos = pos
    elif face =="south":
      old_pos = pos[:]
      pos[1]-=distance
      new_pos = pos
    else:
      old_pos = pos[:]
      pos[0]-=distance
      new_pos = pos
    if old_pos[0] == new_pos[0]:
      if old_pos[1] < new_pos[1]:
        for i in range(old_pos[1]+1,new_pos[1]+1):
          all_pos.append([old_pos[0],i])
      else:
        for i in reversed(range(new_pos[1],old_pos[1])):
          all_pos.append([old_pos[0],i])

    else:
      if old_pos[0] < new_pos[0]:
        for i in range(old_pos[0]+1,new_pos[0]+1):
          all_pos.append([i,old_pos[1]])
      else:
        for i in reversed(range(new_pos[0],old_pos[0])):
          all_pos.append([i,old_pos[1]])
  return pos,all_pos




def getDistanceToHQ():
  return abs(sum(walkingAbout(text)[0]))

def seenBefore():
  walky = []
  for i in walkingAbout(text)[1]:
    if i not in walky:
      walky.append(i)
    else:
      return abs(sum(i))

text = """L1, L3, L5, L3, R1, L4, L5, R1, R3, L5, R1, L3, L2, L3, R2, R2, L3, L3, R1, L2, R1, L3, L2, R4, R2, L5, R4, L5, R4, L2, R3, L2, R4, R1, L5, L4, R1, L2, R3, R1, R2, L4, R1, L2, R3, L2, L3, R5, L192, R4, L5, R4, L1, R4, L4, R2, L5, R45, L2, L5, R4, R5, L3, R5, R77, R2, R5, L5, R1, R4, L4, L4, R2, L4, L1, R191, R1, L1, L2, L2, L4, L3, R1, L3, R1, R5, R3, L1, L4, L2, L3, L1, L1, R5, L4, R1, L3, R1, L2, R1, R4, R5, L4, L2, R4, R5, L1, L2, R3, L4, R2, R2, R3, L2, L3, L5, R3, R1, L4, L3, R4, R2, R2, R2, R1, L4, R4, R1, R2, R1, L2, L2, R4, L1, L2, R3, L3, L5, L4, R4, L3, L1, L5, L3, L5, R5, L5, L4, L2, R1, L2, L4, L2, L4, L1, R4, R4, R5, R1, L4, R2, L4, L2, L4, R2, L4, L1, L2, R1, R4, R3, R2, R2, R5, L1, L2"""


print(getDistanceToHQ())
print(seenBefore())
