from itertools import combinations 

def squareSum(x,power,value):
    result = 0
    for i in x:
        result += i**power

        if result > value:
            # print(result)
            return -1
    # print(result)
    return result


value = int(input())
power = int(input())

num = []
for i in range(1,int(value**(1/float(power)))+1):
    num.append(i)

count = 0

i = 1
while i < int(value**(1/float(power)))+1:
    for j in combinations(num, i):
        # print(j)
        if squareSum(list(j),power,value)==value:
            print(j)
            # print('Success')
            count+=1
            # break
    i += 1
print(count)
    
'''
version 2

from itertools import combinations 

def squareSum(x,power,value):
    result = 0
    x.sort(reverse=True)
    for i in x:
        result += i**power
        if result > value:
            return -1
    return result


value = int(input())
power = int(input())

num = []
for i in range(1,int(value**(1/float(power))+1)):
    num.append(i)

count = 0
for i in range(1,int(value**(1/float(power))+1)):
    for j in combinations(num, i):
        if squareSum(list(j),power,value)==value:
            count+=1

print(count)

'''