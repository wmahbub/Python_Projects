# Libraries

import math

# Formulas

def square_num(a):
    """ Returns the square number. """
    
    answer= a**2
    
    return answer

def sum_of_squares(a,b):
    """ Sums squares of numbers between (a) and (b). """
    
    total=0
    
    for i in range(a,b+1):
        ans= square_num(i)
        total += ans
    
    return total


def sum_of_only_squares(a,b):
    """ Sums only square numbers between (a) and (b)."""
    
    total = 0
    
    for i in range(a, b+1):
        if is_square_num2(i) == True:
            total += i
    
    return total 


def is_square_num1(a):
    """ Checks if the number is a square number or not. """
    lst = []
    
    for i in range(1,a+1):
        i = i**2
        list.append(i)
    
    if a in lst:
        return True
    else:
        return False


def is_square_num2(a):
    """ Checks if the number is a square number or not. """
    
    ans = math.sqrt(a)
    f, i = math.modf(ans)
    
    if f == 0 :
        return True
    else:
        return False


def triangle_num(a):
    """ Returns the triangle number. """
    lst = []
    
    for i in range(1,a+1):
        lst.append(i)
    
    return sum(lst)        
    
    
def is_triangle_num(a):
    """ Checks if the number is a triangle number or not. """
    lst = []
    
    for i in range(1,a+1):
        lst.append(triangle_num(i))
    
    if a in lst:
        return True
    else:
        return False 


def circle_slices(a):
    """ Calculates the maximum number of pieces that can be made from (a) slices. """
    
    #assert a == int
    
    if a >= 0:
        ans = ( (a**2) + a + 2 )/2
        
        return ans
    
    else:
        return "Slices must be greater than or equal to 0"
    
def list_slices(a,b):
    """ Lists the number of pieces that can be made from (a) to (b) slices. """
    
    slices = []
    
    for i in range(a, b+1):
        ans = circle_slices(i)
        slices.append(ans)
    
    return slices 
    

def check_pieces(a):
    """ jf """
    
    pieces= []
    
    for i in range(a+1):
        ans= circle_slices(i)
        pieces.append(ans)
    
    if a in pieces:
        return True
    
    else:
        return False

def num_slices(a):
    """ Returns the number of slices you would need to generate (a) pieces. """
    
    d= (8*a) - 7
    
    if d < 0:
        return "No real solution can be found"
    
    if d == 0:
        return -1
    
    else:
        m = (-1 + math.sqrt(d) ) / 2
        # n = (-1 - math.sqrt(d) ) / 2 (produces negative number)
        f,i = math.modf(m)
        
        i =  int(i)
        
        if f != 0:
            lower = circle_slices(i)
            upper = circle_slices(i+1)
        
            msg= "Cannot make " + str(a) + " pieces. You can make " + str(lower) + " pieces with " + str(i) + " slices, or make " + str(upper) + " pieces with " + str(i+1) + " slices."

            return msg
        
        else:
            return i

def catalan_number(a):
    """ Returns Catalan number for ath term. """
    
    assert a >= 0
    
    ans = math.factorial((2*a)) / ( math.factorial(a+1) * math.factorial(a) )
    
    return ans

def is_catalan(a):
    """ Checks to see if a number is Catalan or not."""
    
    assert a >= 0
    
    for i in range(0,a+1):
        if catalan_number(i) == a:
            return True
    
    return False

