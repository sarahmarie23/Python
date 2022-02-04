# CS 232 Spring 2022 – Week 03 Lab
# Sarah Jimenez and Kevin Fasteen

import random

# Problem 1
# mults_of_7 takes in a list (any length, any data type)
# for every element, if it can be converted to a number,
# and is a multiple of 7, add it to a list and return the list
# if not, print a message saying that it couldn't be converted

def mults_of_7(a_list):
    solution_list = []
    for i in a_list:
        try:
            int(i)
            if(i % 7 == 0):
                solution_list.append(i)
            else:
                print(i, " is not a multiple of 7")
            
        except:
            print(i, " couldn't be converted to an int")    

    return solution_list        

# Problem 2
# dice_count simulates rolling 60, 6-sided dice. It counts
# how many times each side was rolled and prints the side
# that was rolled the most. If there is a tie between two
# or more sides, then print out all the tied sides

def dice_count():
    dice_list = []
    for i in range(0, 60):
        dice_list.append(random.randint(1, 6))

    print(dice_list)
    print(len(dice_list), " is the length")

    
    count_list = [0]
    # testing was done here
    #for i in range(1, 7):
    #    count = dice_list.count(i)
    #    count_list.append(count)
    #    print(i , " rolled ", count, "  times ")
        
    max_value = max(count_list)
    for i in range(1, 7):
        if count_list[i] == max_value:
            print(i, " rolled ", max_value , " times ")

# Problem 3
# caesar_cipher takes in a string and converts it
# to all caps, shifts each letter by 3, (only letters,
# not non-numeric characters) and prints the
# encoded string

def caesar_cipher(a_string):
    
    converted_list = []
    a_string = a_string.upper()
        
    for char in a_string:
        if char.isalpha():
            if char  == 'X' or char == 'Y' or char == 'Z':
                converted_list.append(chr(ord(char) - 23))
            else:
                converted_list.append(chr(ord(char) + 3))
        else:
            converted_list.append(char)
            
            
    new_string = ""
    ''.join(converted_list)
    print(''.join(converted_list))
