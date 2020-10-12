'''
from random import randrange

def magic8Ball():
    answers = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.", "Yes.", "Yes – definitely.", "You may rely on it."]
    choice = randrange(len(answers))
    print(answers[choice])

magic8Ball()
'''
'''

def great_magician(name):
    return "The Great " + name + "!"
    
print(great_magician("Houdini")) # The Great Houdini!
print(great_magician("David Blaine")) # The Great David Blaine!

'''
'''
def sum(num1, num2 = 0):
    result = num1 + num2
    return result

total = sum(1, 2)
print(total) # 3

total = sum(3, 5)
print(total) # 8

total = sum(-2, 2)
print(total) # 0

total = sum(1)
print(total)
'''

'''
import random

# random.seed(1) # Will generate a set of random number values the first time you run the code
# If you run your program again, you'll get the same random number again

rand = random.random()        
print(rand) # A random float between 0.0 and 0.999999999999

rand = random.uniform(1, 10) 
print(rand) # A random float between 1.0 and 9.99999999999

rand = random.randint(1, 10)
print(rand) # A random integer from 1 to 10, endpoints included

rand = random.randrange(0, 101, 2) 
print(rand) # A random even integer from 0 to 100

rand = random.choice('abcdefghij')  
print(rand) # Chooses a random element

items = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(items)
print(items) # Randomizes a list

rand = random.sample(items,  3)
print(rand) # Choose 3 random elements from a list

'''

'''
1. Define the functions name
2. global variables
3. indent code
4  call the function
5. put the appropriate input values.
'''
'''
def calculate_tuition_increases(tuition, percent_increase, number_of_years):
    for i in range (number_of_years):
        tuition *= 1 + percent_increase
        result = "In " + str(i + 1)
        result += " year" if i == 0 else " years"
        result += ", the tuition will be $"+ format(tuition, ",.2f") + "."
        print(result)
    print()

calculate_tuition_increases(8000, 0.03, 5)
calculate_tuition_increases(8000, 0.045, 2)
calculate_tuition_increases(8000, 0.02, 4)

calculate_tuition_increases(8000, 0.02, 4)
    int
'''

'''
transactionsThisMonth = 1
accountBalance = 555.55
firstName = "Marc"
lastName = "Hauschildt"
accountNumber = "415"
pin = "1234"
active = True
PROCESSING_FEE = 2.00
INTEREST_RATE = 0.019

accountNumberInput = input("What is your account number? ")
attempts = 1
totalAttempts = 3
while(attempts < totalAttempts and accountNumberInput != accountNumber):
    print("That account number was not found. You have", totalAttempts - attempts, " attempt(s) remaining.\n")
    accountNumberInput = input("What is your account number? ")
    attempts += 1
if(accountNumberInput == accountNumber):
    pinInput = input("What is your PIN? ")
    attempts = 1
    while(attempts < totalAttempts and pinInput != pin):
        print("Incorrect PIN. You have", totalAttempts - attempts, " attempt(s) remaining.\n")
        pinInput = input("What is your PIN? ")
        attempts += 1
    if(pinInput == pin):
        print("\nWelcome to the bank, " + firstName + " " + lastName)
        print("Your account balance is $" + format(accountBalance, ",.2f"))
        if(accountBalance > 0):
            print("\nThis transaction includes a $" + format(PROCESSING_FEE, ".2f"), "processing fee.")
            withdrawInput = float(input("\nHow much would you like to withdraw? ")) + PROCESSING_FEE
            while(withdrawInput > accountBalance):
                print("Sorry, you don't have enough money to make that withdraw.")
                withdrawInput = float(input("\nHow much would you like to withdraw? ")) + PROCESSING_FEE
            if(withdrawInput <= accountBalance):
                accountBalance = accountBalance - withdrawInput
                interestEarned = accountBalance * (INTEREST_RATE / 12)
                print("Your account earned $" + format(interestEarned, ".2f"), "in interest this month.")
                accountBalance = accountBalance + interestEarned
                print("\nYour updated account balance is $" + format(accountBalance, "5.2f"))
                transactionsThisMonth += 1
                print("You have made", str(transactionsThisMonth), "transactions this month.")
        else:
            print("Sorry, you don't have enough money to make a withdraw.")
        ratingInput = int(input("\nRate your experience today (1-Bad, 5-Great): "))
        while(ratingInput < 1 or ratingInput > 5):
            ratingInput = int(input("\nInvalid input. Rate your experience today (1-Bad, 5-Great): "))
        if (ratingInput >= 4):
            print("We're glad to serve you!")
        elif (ratingInput >= 2):
            print("Sorry that your experience wasn't the best today.")
        else:
            print("We'll do better next time!")
print("\nGoodbye.") 
'''

from helpers import *

def getDataFromDatabase():
  accountNumber = "9999"
  pin = "1234"
  transactionsThisMonth = 1
  accountBalance = 555.55
  firstName = "Marc"
  lastName = "Hauschildt"
  active = True
  return [accountNumber, pin, active, firstName, lastName, accountBalance, transactionsThisMonth]

def greetCustomer(name, accountBalance):
  print("\nWelcome to the bank,", name)
  print("Your account balance is $" + format(accountBalance, ",.2f"))

def addInterest(accountBalance):
  INTEREST_RATE = 0.019
  interestEarned = accountBalance * (INTEREST_RATE / 12)
  if(interestEarned > 0):
    print("Your account earned $" + format(interestEarned, ".2f"), "in interest.")
  return interestEarned

def endTransaction(accountBalance, transactionsThisMonth):
  print("\nYour updated account balance is $" + format(accountBalance, "5.2f"))
  print("You have made", str(transactionsThisMonth), "transactions this month.")
  ratingInput = getNum("Rate your experience today (1-Bad, 5-Great): ", 1,5, float("inf"), True)
  if (ratingInput >= 4):
      print("We're glad to serve you!")
  elif (ratingInput >= 2):
      print("Sorry that your experience wasn't the best today.")
  else:
      print("We'll do better next time!")

def main():
  accountNumber = getDataFromDatabase()[0]
  pin = getDataFromDatabase()[1]
  while (True):
    validAccountNumber = validateUserString("What is your account number?", [accountNumber], False, 3, "That account number was not found.")
    if (not (validAccountNumber)):
      break
    validPIN = validateUserString("What is your PIN?", [pin], False, 3, "Incorrect PIN.")
    if (not (validPIN)):
      break
    customerData = getDataFromDatabase()
    activeCustomer = customerData[2]
    if (not (activeCustomer)):
      print("Your account is not active.")
      break
    customerName = customerData[3] + " " + customerData[4]
    accountBalance = customerData[5]
    greetCustomer(customerName, accountBalance)
    if (accountBalance <= 0):
      print("Sorry, you don't have enough money to make a withdraw.")
      break
    PROCESSING_FEE = 2.00
    print("\nThis transaction includes a $" + format(PROCESSING_FEE, ".2f"), "processing fee.")
    withdrawAmount = getNum("How much would you like to withdraw? ", 0, accountBalance - PROCESSING_FEE, float("inf"), False, "Cannot process that withdraw amount.")
    accountBalance = accountBalance - withdrawAmount - PROCESSING_FEE
    # accountBalance += addInterest(accountBalance)
    transactionsThisMonth = customerData[6] + 1
    endTransaction(accountBalance, transactionsThisMonth)
    break
  print("\nGoodbye.")

main()