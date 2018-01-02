"""
http://adventofcode.com/2017/day/16
"""
import string
import copy


def createDance(some_string):
    unparsed = [d for d in some_string.split(",")]
    parsed = []
    for m in unparsed:
        if "/" in m:
            split = m.strip('\n').split('/')
            parsed.append((split[0][0],split[0][1:],split[1]))
        else:
            parsed.append((m[0],int(m[1:])))
    return parsed


def dance(some_string):
    dance_moves = createDance(some_string)
    p = string.ascii_lowercase[:16]
    seen = []
    for i in range(1000000):
        if p in seen:
            return seen[1000000000 % len(seen)]
        else:
            seen.append(p)
            for m in dance_moves:
                if m[0] == 's':
                    p = p[-m[1]:]+p[:-m[1]]
                else:
                    if m[0] == 'x':
                        pos_a,pos_b,char_a,char_b = int(m[1]),int(m[2]),p[int(m[1])],p[int(m[2])]
                    else:
                        pos_a,pos_b,char_a,char_b = p.index(m[1]),p.index(m[2]),m[1],m[2]
                    if pos_a < pos_b:
                        first = p[:pos_a]
                        second = p[pos_a+1:pos_b]
                        third = p[pos_b+1:]
                        p = first+char_b+second+char_a+third
                    else:
                        first = p[:pos_b]
                        second = p[pos_b+1:pos_a]
                        third = p[pos_a+1:]
                        p = first+char_a+second+char_b+third
    return p

unit_test1a = "s1,x3/4,pe/b"
final_test1 = open('day16_inputs.txt').read()
print(dance(final_test1))
