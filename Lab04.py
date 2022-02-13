# CS 232 Spring 2022 -  Week 04 Lab
# Sarah Jimenez and Kevin Fasteen

# Problem 1
# practice working with dictionaries

PRICE_DICT = {'apples' : 3.79, 'bananas' : 1.29, 'pears' : 2.49,
                  'carrots' : 2.29, 'broccoli' : 3.29}


def problem_1():

    # a
    print("There are ", len(PRICE_DICT), " pairs in the dictionary")

    # b
    print("The value for carrots is ", PRICE_DICT.get('carrots'))

    # c
    print(list(PRICE_DICT.keys()))

    # d
    print(list(PRICE_DICT.values()))

    # e
    PRICE_DICT.update({'apples' : 1.99})

    # f
    PRICE_DICT['grapes'] = 2.68

    # g
    'cauliflower' in PRICE_DICT

    # h
    del PRICE_DICT['broccoli']

    # i

    total = 0
    for i in PRICE_DICT.values():
        total += i
        
    print(total)



# Problem 2
# max_coordinate_value takes in a dictionary (of letters and number tuples)
# and an int (0 or 1) and returns the maximum x or y value (0 for X, 1 for y)


test_dict = { 'a': (4, 3), 'b': (1, 2), 'c': (5, 1), 'd': (3, 6) }

def max_coordinate_value(test_dict, test_int):
    my_list = []

    for i in test_dict.values():
        my_list.append(i[test_int])

    return max(my_list)



# Problem 3
# distance asks the user for two points and prints the distance between
# those two points. The points are stored as letters so this problem assumes
# the user is giving valid input


import math

def distance(test_dict):

    point_1 = input("Which is your first point? ")
    point_2 = input("Which is your second point? ")
    
    p_1 = test_dict.get(point_1)
    p_2 = test_dict.get(point_2)

    x_1 = p_1[0]
    y_1 = p_1[1]

    x_2 = p_2[0]
    y_2 = p_2[1]

    distance = ((x_2 - x_1)**2 + (y_2 - y_1)**2)**.5

    print("The distance between points " , point_1, " and " , point_2, " is "
          , distance, " units")
