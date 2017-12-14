"""
http://adventofcode.com/2017/day/10
"""

import numpy as np
from functools import reduce

def knotHash(inputs):
  input_lengths = [int(i) for i in convertToAscii(inputs).split(",")]
  output_list = list(range(256))
  skip_size = 0
  pos = 0
  for erer in range(64):
    for l in input_lengths:
      loop_list = output_list[pos:]+output_list[:pos]
      rev_list = list(reversed(loop_list[:l]))
      insertion_pos = pos
      for r in rev_list:
        try:
          output_list[insertion_pos] = r
          insertion_pos+=1
        except IndexError:
          insertion_pos = 0
          output_list[insertion_pos] = r
          insertion_pos += 1
      jump = l+skip_size
      index_value = pos
      for _ in range(jump):
        try:
          index_value+=1
          output_list[index_value]
        except IndexError:
          index_value = 0
      pos = index_value
      skip_size+=1

  output_list = convertToSparse(output_list)
  output_list = convert2Hex(output_list)

  return output_list


def convertToAscii(string):
  ascii_string = ''
  for c in string:
    ascii_string += str(ord(c))+","
  return ascii_string+'17,31,73,47,23'

def convert2Hex(sparselist):
  hexed = ''
  for xor in sparselist:
    if len(hex(xor)) == 3:
      hexed+='0'+hex(xor).replace('0x', '')
    else:
      hexed+=hex(xor).replace('0x', '')
  return hexed

def convertToSparse(denselist):
  output = []
  i = 0
  for _ in range(16):
    output.append(reduce(lambda x,y: x ^ y,denselist[i:i+16]))
    i+=16
  return output

testdata = "1,2,3"

#print(knotHash("189,1,111,246,254,2,0,120,215,93,255,50,84,15,94,62"))
#print(knotHash('flqrgnkx-0'))
"""
The empty string becomes a2582a3a0e66e6e86e3812dcb672a272.
AoC 2017 becomes 33efeb34ea91902bb2f59c9920caa6cd.
1,2,3 becomes 3efbe78a8d82f29979031a4aa0b16a9d.
1,2,4 becomes 63960835bcdc130f0b66d7ff4f6a5a8e.
"""

"""800db3a508a45d65d389c36ffb4b6a23"""
