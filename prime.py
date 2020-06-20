# Libraries

import numpy as np

# Prime number formulas

def is_prime(a):
    """ Determines whether integer is prime or not. """
    div=[]
    
    if a<=1:
        return False    
    
    else:
        for i in range(1,a+1):
            if a % i==0:
                div.append(i)
        if len(div) != 2:
            return False
        else:
            return True


def sum_prime(a,b):
    """ Adds prime numbers between (a) and (b). """
    
    num=[]
    
    for i in range(a,b+1):
        if is_prime(i)== True:
            num.append(i)
    
    return sum(num)


def prod_prime(a, b):
    """ Multiplies prime numbers between (a) and (b). """
    
    num = []
    
    for i in range(a, b + 1):
        if is_prime(i) == True:
            num.append(i)
    
    return np.prod(num)


def list_prime(a, b):
    """ Lists all prime numbers between (a) and (b). """
    
    num = []
    
    for i in range(a, b + 1):
        if is_prime(i) == True:
            num.append(i)
    
    return num


def fact_prime(a):
    """ Lists the prime factors of a number (a). """
    
    fact=[]
    
    for i in range(1, a + 1):
        if a % i == 0 and is_prime(i)== True:
            fact.append(i)
    
    return fact

                
