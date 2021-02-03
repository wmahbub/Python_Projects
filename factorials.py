import even_odd

def factorial(n):
    """ returns the factorial of a number (n). """
    
    if n==1 or n==0:
        return 1
    
    else:
        rec= n * factorial(n-1)
        
        return rec
    
def double_factorial(n):
    """ returns the even or odd factorials of a number (n). """
    
    if even_odd.is_even(n)== True:
        
        if n <=1:
            return 1
        
        else:
            rec = n * double_factorial(n-2)
            
            return rec
    
    else:
        if n <= 1:
            return 1
        
        else:
            rec= n * double_factorial(n-2)
            
            return rec
        

