# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
# Evaluate the expression. Return an integer that represents the value of the expression.
# Note that:
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
import math

def evalRPN(tokens: list[str]) -> int:
    #this solution have a O(n) time complexity
    stx = []
    for val in tokens:
        if val not in ["+", "-", "*", "/"]:
            stx.append(int(val)) #if val is a number add to the stack
        else:
            if len(stx) < 2: #be sure if we have almost 2 elements in stack
                raise ValueError("Expresión RPN inválida")

            #pop the last 2 elements
            b = stx.pop() 
            a = stx.pop()

            #make the corresponding operation
            if val == "+":
                stx.append(a + b)
            elif val == "-":
                stx.append(a - b)
            elif val == "*":
                stx.append(a * b)
            elif val == "/":
                stx.append(int(a / b))
    #at the last we should have one element in the stack
    return stx[0]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
input()
print(evalRPN(tokens))