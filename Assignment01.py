# CS 232 Python
# Assignment 01
# Sarah Jimenez
# Last modified 2/6/22

import math

# Problem 1
# multiples_in_range: number, number, number -> number
# purpose: expects 3 numbers (int or float) and returns the
#          quantity of values that are between the 2nd and 3rd number,
#          that are multiples of the first number
# side effects: prints each number
# assumptions: all 3 arguments are int or float, begin <= end


def multiples_in_range(step, begin, end):
    count = 0

    if (step or begin or end) < 0:
        print("You entered a negative number!")
    else:
        for i in range(begin+step, end, step):
            print(i)
            count += 1

    return count



# Problem 2
# letter_grade: float -> string
# purpose: expects a float (greater than or equal 0.0) and returns the
#          corresponding letter grade (A - F)
# side effects: prints the grade, with + or - if needed
# assumptions: the float is >= 0.0


def letter_grade(grade):

    letter = ""

    if grade >= 90:
        print("Excellent! You got an A", end="")
        letter = "A"

    elif grade >= 80:
        print("Good job! You got a B", end="")
        letter = "B"
        
    elif grade >= 70:
        print("Nice! You got a C", end="")
        letter = "C"
        
    elif grade >= 60:
        print("You got a D", end="")
        letter = "D"

    else:
        print("You got an F")
        letter = "F"

    if grade >= 60:
        grade = math.floor(grade)
        if grade >= 100.0 or grade % 10 in range(7, 10):
            print("+")
        elif grade % 10 in range(0, 3):
            print("-")
        else:
            print("")
        

    return letter



# Problem 3
# bump_it: object -> object
# purpose: expects any data type and "bumps it" if it is an int or float,
#          adds a "!" if it is a string, changes it to the opposite boolean
#          if it is a boolean, and if anything else, returns the original
#          input that it was given
# side effects: none
# assumptions: none, the input can be of any data type


def bump_it(input):
    if type(input) == int:
        input += 1
    elif type(input) == float:
        input += 0.1
    elif type(input) == str:
        input += "!"
    elif type(input) == bool:
        input = not input

    return input



# Problem 4
# my_nickname: string -> string
# purpose: returns a nicknamed version of a string, if the name is long enough.
#          Also capitalizes it if needed
# side effects: prints the name to the screen
# assumptions: the name is a string and a one-word first name


def my_nickname(name):
    name = name.capitalize()
   
    if len(name) >= 5:
        if name.find("y") == 4:
            name = name[0:4]
        else:
            name = name[0:5]
            name += "y"

    print(name)
    return name



# Problem 5
# flip_case: string -> string
# purpose: changes the string to the opposite case if every letter is in the same
#          case, and if it is mixed case, it returns the string with the first
#          letter changed to the opposite case
# side effects: none, it doesn't print anything
# assumptions: the input is a string


def flip_case(input):
    answer = ""
    
    if input.isupper():
        answer = input.lower()
    elif input.islower():
        answer = input.upper()
    else:
        first_letter = input[0:1]
        if first_letter.isupper():
            first_letter = first_letter.lower()
            
        else:
            first_letter = first_letter.upper()
        answer += first_letter
        answer += input[1:]

    return answer



# Problem 6
# fibonacci_list: integer -> list
# purpose: returns a list of Fibonnacci numbers up to the length of the integer
#          but only if a valid integer was given
#          [0, 1, 1, 2, 3, 5, 8] would be the first 7 numbers
# side effects: prints an error message if the given number is less than 2
# assumptions: none, because it checks for invalid input


def fibonacci_list(fib_length):
    fib_list = []
    
    if fib_length < 2 or type(fib_length) !=  int:
        print("Invalid input!")
        return fib_list
    
    fib_list = [0, 1]
    
    for i in range(2, fib_length):
        fib_list.append(fib_list[i-1] + fib_list[i-2])

    return fib_list
