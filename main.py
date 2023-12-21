"""
Name: Lenny Muldoon

Desc: This is a basic calculator program for me to learn python syntax
"""
import math

answer = 0
quit = False

def add(inputNum, currentNum):
    return currentNum + inputNum

def subtract(inputNum, currentNum):
    return currentNum - inputNum

def multiply(inputNum, currentNum):
    return currentNum * inputNum

def divide(inputNum, currentNum):
    return currentNum / inputNum


while not quit:
    choice = int(input("What operation would you like to do? 1 for addition 2 for subtraction 3 for multiplication 4 for division 5 for quit"))
    if choice == 1:
        print("Total is currently", answer)
        inputNum = int(input("What number would you like to add to your total?"))
        answer = add(inputNum, answer)
        print("New total is", answer)
    elif choice == 2:
        print("Total is currently", answer)
        inputNum = int(input("What number would you like to subtract to your total?"))
        answer = subtract(inputNum, answer)
        print("New total is", answer)
    elif choice == 3:
        print("Total is currently", answer)
        inputNum = int(input("What number would you like to multiply to your total?"))
        answer = multiply(inputNum, answer)
        print("New total is", answer)
    elif choice == 4:
        print("Total is currently", answer)
        inputNum = int(input("What number would you like to divide to your total?"))
        answer = divide(inputNum, answer)
        print("New total is", answer)
    else:
        quit = True