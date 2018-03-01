######
#
# cost_pizza.py
#
# Created by: Sebastian N 
# Created on: February 28
#
# This program calculates the cost of a pizza
#######

def cost_pizza(diameter_passed_in):
    # Variables
    subtotal = (0.75 + 1.00 + (diameter_passed_in * 0.50))
    HST = (subtotal * 0.13)
    Total = subtotal + HST
    # Printing
    print 'Subtotal is: $', subtotal
    print 'The taxt is: $', HST
    print 'The total is: $', Total

    return Total;

diameter = input('Enter the diameter of your pizza: ')
diameter_as_number = float(diameter)
cost = cost_pizza(diameter_as_number)


