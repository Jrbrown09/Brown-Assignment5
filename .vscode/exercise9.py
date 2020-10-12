from helpers import *

'''
Exercise 9
Monthly Sales Tax

This program takes the monthly sales amount, entered by the user, and calculates the monthly county
and state sales tax. At the end, it computes the sum of these two tax amounts

'''

'''
Defines the 'main' function

'''
def main():
    
    monthly_sales_entered = get_monthly_sales() 
    county_sales_tax = get_county_sales_tax(monthly_sales_entered)
    state_sales_tax = get_state_sales_tax(monthly_sales_entered)
    total_sales_tax = get_total_sales_tax(state_sales_tax, county_sales_tax)
    display_tax_amounts(county_sales_tax, state_sales_tax, total_sales_tax)

''' 
Defines the monthly sales function.
User enters the monthly sales.
@return the monthly sales
'''
def get_monthly_sales():
    monthly_sales = getFloat("Enter the monthly sales amount: ")
    return monthly_sales

'''
Create global variable for the county sales tax rate
'''
COUNTY_SALES_TAX_RATE = .025

'''
Defines the county sales tax function
@global COUNTY_SALES_TAX_RATE
@param monthly_sales
@return the county sales tax amount
'''
def get_county_sales_tax(monthly_sales):
    global COUNTY_SALES_TAX_RATE
    county_sales_tax = monthly_sales * .025
    return county_sales_tax

'''
Create global variable for the state sales tax rate
'''
STATE_SALES_TAX_RATE = .05 

'''
Defines the state sales tax calculation function
@global STATE_SALES_TAX_RATE
@param monthly_sales
@return the state sales tax amount
'''
def get_state_sales_tax(monthly_sales):
    global STATE_SALES_TAX_RATE
    state_sales_tax = monthly_sales * .05
    return state_sales_tax

'''
Defines the function that calculates the total sales tax function
@param county_sales_tax
@param state_sales_tax
@return total sales tax amount
'''
def get_total_sales_tax(county_sales_tax, state_sales_tax):
    total_sales_tax = county_sales_tax + state_sales_tax
    return total_sales_tax

'''
Defines the function that displays the tax amounts for the county, state, and total tax owed.
@param county_sales_tax
@param state_sales_tax
@param total_sales_tax

'''
def display_tax_amounts(county_sales_tax, state_sales_tax, total_sales_tax):
    print("County sales tax is: $", format(county_sales_tax, ",.2f"))
    print("State sales tax is: $", format(state_sales_tax, ",.2f"))
    print("Total sales tax is: $", format(total_sales_tax, ",.2f"))

'''
Call the main function
''' 
main()