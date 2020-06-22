# Libraries

import numpy as np

# Formulas

def fib(a):
    """ Returns Fibonacci sequence term. """
    
    seq=[1,1]
    
    if a==0 or a==1 or a==2:
        return 1
    
    else:
        lst= range(a)
        for i in lst[2 : ]:
            term= seq[i-1] + seq[i-2]
            seq.append(term)
        return seq[a-1] 
    

def fib_list(a,b):
    """ Returns Fibonacci sequence between terms a and b, where b > a . """
    
    if a==0 or b==0:
        return "(a) and (b) must be greater than 0"
    
    elif b < a:
        return "(b) must be greater than (a)"
    
    else:
        seq = [1, 1]
        
        lst = range(b)
        for i in lst[2 : ]:
            term = seq[i - 1] + seq[i - 2]
            seq.append(term)
        
        return seq[a - 1: b] 


def fib_sum(a,b):
    """ Returns sum of Fibonacci sequence between terms (a) and (b). """
    
    if a == 0 or b == 0:
        return "(a) and (b) must be greater than 0"
    
    elif b < a:
        return "(b) must be greater than (a)"
    
    else: 
        seq = [1, 1]
    
        lst = range(b)
        for i in lst[2 : ]:
            term = seq[i - 1] + seq[i - 2]
            seq.append(term)
        
        return sum( seq[a - 1: b] )


def fib_prod(a, b):
    """ Returns product of Fibonacci sequence between terms (a) and (b). """
    
    if a == 0 or b == 0:
        return "(a) and (b) must be greater than 0"
    
    elif b < a:
        return "(b) must be greater than (a)"
    
    else: 
        seq = [1, 1]
    
        lst = range(b)
        for i in lst[2 : ]:
            term = seq[i - 1] + seq[i - 2]
            seq.append(term)
        
        return np.prod(seq[a - 1: b])