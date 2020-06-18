def c_to_f(a):
    """ Converts temperature in Celsius to Fahrenheit. """
    
    f = (a * 9/5) + 32
    
    return round(f,2)

def f_to_c(a):
    """ Converts temperature in Fahrenheit to Celsius. """
    
    c = (a- 32) * (5/9)
    
    return round(c,2)

