def c_to_f(a):
    """ Converts temperature in Celcius to Faranhite """
    
    answer = (a * 9/5) + 32
    
    return answer

def f_to_c(b):
    """ Converts temperature in Farenhite to Celcius """
    
    answer = (b- 32) * (5/9)
    
    return answer

c_to_f(4)

f_to_c(10)