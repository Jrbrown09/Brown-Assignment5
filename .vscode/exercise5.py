from helpers import *

'''
Exercise 5
Property Tax

This program calculates the assessment value and the property tax from the property value entered
by the user
'''

'''
Defines the main function

'''
def main():
    property_value_entered = get_property_value()
    assessment_value = get_assessment_value(property_value_entered)
    property_tax = get_property_tax(assessment_value)
    display_output(property_value_entered, assessment_value, property_tax)

'''
Defines the function that gets the property value from the user
@ returns the property value entered by the user
'''
def get_property_value():
    property_value = getFloat("What is the value of your property? $")
    return property_value

'''
Defines the global variable for the assessment value rate
'''
ASSESSMENT_VALUE_RATE = .60

'''
Defines the function that calculates the assessment value of the user's property
@param property_value
@return assessment_value (the value of the user's property entered)
'''
def get_assessment_value(property_value):
    assessment_value = property_value * ASSESSMENT_VALUE_RATE
    return assessment_value

'''
 Defines the global variable for the property tax rate
'''
PROPERTY_TAX_RATE = .72

'''
Defines the function that calculates the property tax for the user's property
@global PROPERTY_TAX_RATE
@param assessment_value
@return property_tax
'''
def get_property_tax(assessment_value):
    global PROPERTY_TAX_RATE 
    property_tax = (assessment_value / 100) * PROPERTY_TAX_RATE
    return property_tax

'''
Defines the function that displays the output for the property value, assessment value, and the property
tax that is calculated.
@param property_value_entered
@param assessment_value
@param property_tax
'''
def display_output(property_value_entered, assessment_value, property_tax):
   print("The value of the property that you have entered is: $", format(property_value_entered, ",.2f"))
   print("The assessment value of your property is: $", format(assessment_value, ",.2f"))
   print("The property tax that you owe is: $", format(property_tax, ",.2f"))

'''
Calls the 'main' function
'''
main()