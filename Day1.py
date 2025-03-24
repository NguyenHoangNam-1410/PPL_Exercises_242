import math

def area(n):
    if(n<0):
        return -1
    else:
        return n*n*math.pi
    
def check(lst,n):
    for num in lst:
        if(num<=n): 
            return False
    return True

def gcd(a,b):
    while a!=b:
        if(a > b):
            a -= b
        else:
            b -= a
    return a

def listAndTuple():
    num = input()
    num_lst = num.split(",")
    num_tuple = tuple(num_lst)
    print(num_lst)
    print(num_tuple)

def product(lst):
    prod = 1
    for num in lst:
        prod *= num
    return prod

def sum_of_cube(n):
    sum = 0
    for num in range(n):
        sum+= num*num*num
    return sum
    