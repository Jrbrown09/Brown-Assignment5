from helpers import *
import random

'''
Exercise 11
Math Quiz

This program will prompt the user to enter a the answer for a math problem asking for the sum of two 
random positive integers.
'''

'''
Defines the 'main' function 
@param user_answer_entered
@param problem_solution
'''
def main():
    user_answer_entered = get_user_answer()
    problem_solution = calculate_actual_answer() 
    check_user_answer(user_answer_entered, problem_solution)      

'''
Defines the global variables that will be used throughout the program.
'''
addend_1 = random.randint(1, 500)
addend_2 = random.randint(1, 500)

'''
Asks the user for the answer to the addition problem
@global variable addend_1 
@global variable addend_2 
@return the answer that the user entered)
'''

def get_user_answer():
    global addend_1
    global addend_2
    
    user_answer = getNum("Please enter the sum of " + str(addend_1) + " + " +  str(addend_2) + ": ")
    return user_answer

'''
Defines the function that calculates the solution to the addition problem.
This function calculates and returns the solution.

@global variable addend_1 
@global variable addend_2
@return the solution to the problem, actual_answer)
'''

def calculate_actual_answer():
    global addend_1
    global addend_2
    
    actual_answer = addend_1 + addend_2
    return actual_answer

'''
Defines the function that checks the answer that the user entered for the addition problem and compares
it to the solution. After the user's answer and the solution are compared, the user will be messaged
according to if they are correct or incorrect.

@param user_answer
@param actual_answer
@function print
'''

def check_user_answer(user_answer, actual_answer):
    if user_answer == actual_answer:
        print("Congratulations, you are correct!")
    else:
        print("You are incorrect. The correct answer is", actual_answer, ".")

'''
Calls the 'main' function.
'''
main()