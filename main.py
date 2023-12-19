"""
Name: Lenny Muldoon

Desc: This is a basic calculator program for me to learn python syntax
"""
import math

answer = 0

def add(inputNum, currentNum):
    return currentNum + inputNum

def subtract(inputNum, currentNum):
    return currentNum - inputNum

def multiply(inputNum, currentNum):
    return currentNum * inputNum

def divide(inputNum, currentNum):
    return currentNum / inputNum


answer += add(4, answer)
print(answer)

answer /= divide(2, answer)
print(answer)

answer -= subtract(1, answer)
print(answer)

answer *= multiply(5, answer)
print(answer)