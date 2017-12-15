"""
http://adventofcode.com/2017/day/10
"""



def duelingGenerators(init_a=0,init_b=0):
    factor_a,div_a,value_a = 16807,4,init_a
    factor_b,div_b,value_b = 48271,8,init_b
    div = 2147483647
    match_c = 0
    # for _ in range(40000000):
    #     value_a = factor_a*value_a % div
    #     value_b = factor_b*value_b % div
    #     if format(value_a,'08b')[-16:] == format(value_b,'08b')[-16:]:
    #         match_c +=1
    for _ in range(5000000):
        value_a = generateNext(value_a,factor_a,div_a)
        value_b = generateNext(value_b,factor_b,div_b)
        if format(value_a,'08b')[-16:] == format(value_b,'08b')[-16:]:
                 match_c +=1
    return match_c



def generateNext(value,factor,dividend):
    while True:
        if (factor*value%2147483647) % dividend == 0:
            return factor*value%2147483647
        else:
            value = factor*value%2147483647



#print(duelingGenerators(512,191))
print(duelingGenerators(512,191))
