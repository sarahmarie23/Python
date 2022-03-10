# CS 232 Spring 2022 – Week 08 Lab
# Given two strings, return which one contains
# more vowels, or 0 if they have an equal amount
# of vowels. (Practice using Counter)

from collections import Counter


def more_vowels(string1, string2):

    vowels = "AEIOUaeiou"
    
    count1 = Counter(string1)
    count2 = Counter(string2)

    sum1 = 0
    sum2 = 0

    for char in count1:
        if char in vowels:
            sum1 += count1[char]


    for char in count2:
        if char in vowels:
            sum2 += count2[char]

    
    if sum1 > sum2:

        return 1

    elif sum1 < sum2:

        return 2

    else:
        return 0
