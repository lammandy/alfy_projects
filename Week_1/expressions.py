import math
from fractions import Fraction


def calc_math_expression(num1, num2, operator):    
    if operator == '+':        
        tot = num1 + num2
    elif operator == '-':
        tot = num1 - num2
    elif operator == '*':
        tot = num1 * num2
    elif operator == ':':
        if num2 == 0:
            return None
        tot = num1 / num2
    else:
        return None
    return tot

def calc_math_expression_from_str(str_input):
    input = str_input.split()
    num1 = float(input[0])
    num2 = float(input[2])
    operator = input[1]
    return calc_math_expression(num1, num2, operator)

def find_largest_and_smallest_numbers(num1=0.0, num2=0.0, num3=0.0):
    nums = (num1, num2, num3)
    return (max(nums), min(nums))
    

def quadratic_equation_solver(a, b, c):
    if a == 0:
        return None, None
    try:
        solution1 = Fraction((-(b) + (math.sqrt(b**2 - 4*a*c))) / (2*a))
    except ValueError:
        solution1 = None
    try:
        solution2 = Fraction((-(b) - (math.sqrt(b**2 - 4*a*c))) / (2*a))
    except ValueError:
        solution2 = None

    if solution1 == solution2:
        return solution1, None
    elif solution1 and solution2:
        return solution1, solution2
    elif solution1 or solution2:
        if solution1:
            return solution1, None
        else:
            return solution2, None
    else:
        return None, None

def quadratic_equation_solver_from_user_input():
    str_input = ''
    str_input = input('quadractic nums a b c: ').split()
    a = float(str_input[0])
    b = float(str_input[1])
    c = float(str_input[2])
    print(quadratic_equation_solver(a, b, c))

def temp_checker(min_temp, temp_1, temp_2, temp_3):
    if temp_1 > min_temp:
        if temp_2 > min_temp:
            return True        
        if temp_3 > min_temp:
            return True        
        else:
            return False
    if (temp_2 > min_temp) and (temp_3 > min_temp):
        return True
    else:
        return False

    