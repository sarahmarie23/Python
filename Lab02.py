# CS 232 Spring 2022 - Week 02 Lab
# Sarah Jimenez

# Problem 1: c_to_f 
# Takes in a float and returns the
# given temperature to fahrenheigh


def c_to_f(input):
    return (input * 1.8) + 32


# Problem 2: c_to_f_check
# Takes in a float and returns the
# given temperature to fahrenheight
# unless it is too low (less than -273.16)
# and then it returns false

def c_to_f_check(input):
    if (input < -273.16):
        print("Temperature is too low!")
        return False

    return (input * 1.8) + 32


# Problem 3: yell_it
# Takes in an input and checks if it
# is a string, if so, it converts to
# upper case

def yell_it(input):
    check = (type(input) == str)
    if (check):
        print(input.upper(), "!!!")
    else:
        print("Not a string!!!")


# Problem 4: divisible_by
# Takes in a positive integer and prints 
# which numbers it is divisible by between
# 2 - 10. Returns nothing

def divisible_by(input):
    check = (type(input) == int)
    if (input < 1):
        print("Invalid input")
    elif (not input):
        print("Not an int!")
    else:
        for i in range(2, 10 + 1):
            if (input%i == 0):
                print(input , " is divisible by ", i )
            else:
                print(input, " is NOT divisible by ", i)

        
# Problem 5: test_demorgan
# Takes two boolean values and returns
# True if DeMorgan's laws are confirmed

def test_demorgan(p, q):
    if (not(p and q) == (not(p)) or (not(q)) and not(p or q) == (not(p)) and (not(q))):
        print("It worked!!")
        return True
    else:
        return False
