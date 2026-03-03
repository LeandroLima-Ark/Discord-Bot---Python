import random


def func_somar(num1:int, num2:int) -> int:
    return num1 + num2

def func_sub(num1:int, num2: int) -> int:
    return num1 - num2

def func_mult(num1: int, num2: int) -> int:
    return num1 * num2

def func_div(num1: int, num2:int) -> int:
    return num1 / num2

def rollnumber(min:int, max:int) -> int:
    return random.randint(min, max)