import hashlib
import string

"""
https://adventofcode.com/2016/day/5
"""

def generatePassword(input_string):
  i = 0
  c = 0
  alphabet = string.ascii_lowercase
  pw_dict = {}
  while c < 10:
    hashed = hashlib.md5((input_string+str(i)).encode('utf-8')).hexdigest()
    if hashed[:5] == '00000' and hashed[5] not in alphabet:
      pos = hashed[5]
      character = hashed[6]
      if pos not in pw_dict:
        pw_dict[pos]=character
        print(pw_dict)
        c+=1
      i+=1
    else:
      i+=1
  return pw_dict


print(generatePassword('uqwqemis'))
