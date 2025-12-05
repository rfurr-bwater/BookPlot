def linear(m,x,b):
    return (m*x)+b

def slope_units(x_units,y_units):
    y_units = y_units.rstrip('s')
    x_units = x_units.rstrip('s')
    return y_units + "/" + x_units

def print_equation(m,b,x_units,y_units):
    print(f"The equation of the line is: y = {m} {slope_units(x_units,y_units)} x + {b} {y_units}")