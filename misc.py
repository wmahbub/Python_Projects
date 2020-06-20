# Formulas

def square_num(a):
    """ Returns the square number. """
    
    answer= a**2
    
    return answer


def is_square_num(a):
    """ Checks if the number is a square number or not. """
    lst = []
    
    for i in range(1,a+1):
        i = i**2
        list.append(i)
    
    if a in lst:
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

        
    
