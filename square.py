def squareSum(x,power=2):
    result = 0
    for i in x:
        result += i**power
    return result

print(squareSum(list((1, 2, 4, 5, 7))))