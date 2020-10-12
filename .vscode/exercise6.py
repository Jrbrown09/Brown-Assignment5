from helpers import *

'''
Exercise 6
Calories from Fat and Carbohydrates

This program calculates the calories from fat and carbohydrates that the user consumed. 
The calorie amounts are calculated using the input from the user in carbohydrates and fat.
'''

'''
Define the 'main' function
'''

def main():
    fat_grams_entered = get_fat_grams()
    carb_grams_entered = get_carb_grams()
    fat_calories = calculate_fat_calories(fat_grams_entered)
    carb_calories = calculate_carb_calories(carb_grams_entered)
    display_calories_output(fat_calories, carb_calories)

'''
Defines the function for the user input of the number of grams of fat entered
return fat_grams, the number of grams of fat entered by the user
'''
def get_fat_grams():
    fat_grams = getFloat("Please enter the number of grams of fat you consume: ")
    return fat_grams

'''
Defines the function for the user input of the number of grams of carbohydrates entered
return carb_grams, the number of grams of carbohydrates entered by the user
'''
def get_carb_grams():
    carb_grams = getFloat("Please enter the number of grams of carbs you consume: ")
    return carb_grams

'''
Defines the function for calculating the number of calories of fat that the user has consumed
@param fat_grams
return fat_calories, calories from fat calculated
'''
def calculate_fat_calories(fat_grams):
    fat_calories = fat_grams * 9
    return format(fat_calories, ",.1f")

'''
Defines the function for calculating the number of calories of carbohydrates that the user has consumed
@param carb_grams
return carb_calories, calories from carbohydrates calculated
'''
def calculate_carb_calories(carb_grams):
    carb_calories = carb_grams * 4
    return format(carb_calories, ",.1f")

'''
Defines the function for displaying the output of the calories from carbohydrates and fat calculated
from the user
@param fat_calories
@param carb_calories
'''    
def display_calories_output(fat_calories, carb_calories):
    print("You have consumed ", str(fat_calories), " calories from fat.")
    print("You have consumed ", str(carb_calories), " calories from carbohydrates.")
    
main()