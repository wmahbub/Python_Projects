# Libraries

import math

# Temperature Formulas

def c_to_f(a):
    """ Converts temperature in Celsius to Fahrenheit. """
    
    f = (a * 9/5) + 32
    
    return round(f,2)

def f_to_c(a):
    """ Converts temperature in Fahrenheit to Celsius. """
    
    c = (a - 32) * (5/9)
    
    return round(c,2)

def c_to_k(a):
    """ Converts temperature in Celsius to Kelvin. """
    
    k = a + 273.15
    
    return round(k,2)

def f_to_k(a):
    
    """ Converst temperature in Fahrenheit to Kelvin. """
    
    k = f_to_c(a) + 273.15
    
    return round(k,2)

def k_to_c(a):
    
    """ Converts temperature in Kelvin to Celsius. """
    
    c = a - 273.15
    
    return round(c,2)

def k_to_f(a):
    
    """ Converts temperature in Kelvin to Fahrenheit."""
    
    f = ( (a - 273.15) * (9/5) ) + 32
    
    return round(f,2)


# Area Formulas

def triangle_area(b,h):
    """ Returns area of triangle with base (b) and height (h)."""
    
    a = b*h*0.5
    
    return round(a,2)

def rectangle_area(a,b):
    
    """ Returns area of rectangle, square and parallelogram, with sides (a) and (b)."""
    
    a = a * b
    
    return round(a,2)

def trapezoid_area(a,b,h): 
    """ Returns area of a trapezoid, with parallel sides (a) and (b), and height (h). """
    
    a = 0.5 * (a + b) * h
    
    return round(a,2)

def ellipse_area(a,b):
    """ Retruns area of an ellipse with semi-major axis (a) and semi-minor axis (b). """
    
    a = math.pi * a * b
    
    return round(a,2)

def circle_area(r):
    """ Returns area of a circle with radius (r). """
    
    a = math.pi * (r**2)
    
    return round(a,2)

def sector_area(angle, r):
    """ Returns area of a circle's sector with interior angle (angle) and radius (r). """
    
    a = (angle/360) * circle_area(r)
    
    return round(a,2)

# Mass Formulas

def kg_to_lb(a):
    """ Converts kilograms (kg) to pounds (lb)."""
    
    lb = a * 2.2046
    
    return round(lb, 2)

def lb_to_kg(a):
    """ Converts pounds (lb) to kilograms (kg)."""
    
    kg = a / 2.2046
    
    return round(kg, 2)

def lb_to_oz(a):
    """ Converts pounds (lb) to ounce (oz). """
    
    oz= a * 16
    
    return round(oz,2)

def kg_to_oz(a):
    """ Converts kilograms (kg) to ounce (oz)."""
    
    oz = a * 35.274
    
    return round(oz, 2)

def oz_to_lb(a):
    """ Converts ounce (oz) to pounds (lb)."""
    
    lb = a / 16
    
    return round(lb,2)

def oz_to_kg(a):
    """ Converts ounce (oz) to kilograms (kg)."""
    
    kg = a / 35.274
    
    return round(kg, 2)

def g_to_oz(a):
    """ Converts grams (g) to ounce (oz)."""
    
    oz = a /28.35
    
    return round(oz,2)

def oz_to_g(a):
    """ Converts ounce (oz) to grams (g). """
    
    g = a * 28.35
    
    return round(g,2)

def g_to_lb(a):
    """ Converts grams (g) to pounds (lb)."""
    
    lb = a / 453.92
    
    return round(lb,2)

def lb_to_g(a):
    """ Converts pounds (lb) to grams (g)."""
    
    g = a * 453.592
    
    return round(g,2)

def uston_to_kg(a):
    """ Converts US Ton (ton) to kilograms (kg)."""
    
    kg = a * 907.185
    
    return round(kg,2)

def kg_to_uston(a):
    """ Converts kilogram (kg) to US Ton (ton). """
    
    ton = a / 907.185
    
    return round(ton,2)

def lb_to_uston(a):
    """ Converts pounds (lb) to US Ton (ton)."""
    
    ton = a / 2000
    
    return round(ton, 2)

def uston_to_lb(a):
    """ Converts US Tons (ton) to pounds (lb)."""
    
    lb = a * 2000
    
    return round(lb, 2)

def uston_to_metton(a):
    """ Converts US Ton (ton) to Metric Ton (metric ton). """
    
    metton = a / 1.10231
    
    return round(metton, 2)
    
def metton_to_uston(a):
    """ Converts Metric Ton (metric ton) to US Ton (ton). """
    
    uston = a * 1.10231
    
    return round(uston, 2)
    

 
    





