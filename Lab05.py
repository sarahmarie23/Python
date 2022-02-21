# CS 232 Spring 2022 – Week 05 Lab
# Sarah Jimenez & Gannon Carroll



# Problem 1

def until_break():
    letter = ""

    while True:
        letter = input("Enter a letter (x to stop) ")
        if letter == 'x':
            break



#Problem 2
    
def all_but_3s(max_value):
    for i in range(0, max_value+1):
        if i%3 == 0:
            continue
        print(i, end=" ")



# Problem 3

def list_all_but_3s(max_value):
    my_list = [i for i in range(0, max_value+1) if not (i%3 == 0)]

    return my_list



# Problem 4

def alpha_dict():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    my_dict = {num : char for (num, char) in zip(range(1, 27), alphabet)}

    return my_dict



# Problem 5

def string_list(*args):
    my_list = []
    for i in args:
        if type(i) == str:
            my_list.append(i)

    return my_list



# Problem 6

def list_at_index(my_tuple, index):
    my_list = []

    for i in my_tuple:
        if index >= len(i):
            return my_list

    my_list = [i[index] for i in my_tuple]
    
    return my_list
    

