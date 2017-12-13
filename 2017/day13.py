from collections import OrderedDict

unit_test1 = """0: 3
1: 2
4: 4
6: 4"""

final_test1 = """0: 4
1: 2
2: 3
4: 4
6: 8
8: 5
10: 6
12: 6
14: 10
16: 8
18: 6
20: 9
22: 8
24: 6
26: 8
28: 8
30: 12
32: 12
34: 12
36: 12
38: 10
40: 12
42: 12
44: 14
46: 8
48: 14
50: 12
52: 14
54: 14
58: 14
60: 12
62: 14
64: 14
66: 12
68: 12
72: 14
74: 18
76: 17
86: 14
88: 20
92: 14
94: 14
96: 18
98: 18"""


def createFirewallList(some_string):
  fw_dict = OrderedDict({int(l.split(': ')[0]):int(l.split(': ')[1]) for l in some_string.split('\n')})
  fw_list =[]
  for l in range(max(fw_dict.keys())+1):
    if l in fw_dict:
      fw_list.append((fw_dict[l]-2)*2+2)
    else:
      fw_list.append(0)
  return fw_list

def computeSeverity(some_string):
  fw_list = createFirewallList(some_string)
  pico = 0
  severity = 0
  for l in fw_list:
    if l != 0:
      if pico%l == 0:
        severity += ((l-2) // 2 + 2)*pico
    pico+=1
  return severity


def breakFirewall(some_string):
  fw_list = createFirewallList(some_string)
  delay = 1
  while True:
    pico = 0 + delay
    for l in fw_list:
      if l != 0:
        if pico%l == 0 and l != 0:
          delay+=1
          break
      pico+=1
    else:
        return(delay)

print(breakFirewall(final_test1))
print(computeSeverity(unit_test1))
