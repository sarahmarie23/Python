# CS 232 Lab 09
# 3/23/22


import os

# Purpose: to practice opening a file and counting letters,
#          words, and sentences, and checking for proper
#          sentence format.

def gettysburg(a_letter):
    count = 0
    
    os.chdir("C:/Users/smj83/Desktop")
    my_file = open("GettysburgAddress.txt", "rt")
    the_g_add = my_file.read()


    g_words = []
    g_words = the_g_add.split()

    
    for word in g_words:
        if word[0] is a_letter:
            count += 1

    if count is 1:
        print("There is one word in the Gettysburg Address that starts with '{}'"
          .format(a_letter))
    elif count > 1:
        print("There are {c} words in the Gettysburg Address that start with '{l}'"
          .format(c=count, l=a_letter))
    else:
        print("There are no words in the Gettysburg Address that start with '{}'"
          .format(a_letter))
    
    my_file.close()



def count_sentencees(a_filename):
    count = 0

    my_file = open(a_filename, "rt")
    sentence_count = my_file.read()

    file_words = []
    file_words = sentence_count.split()

    # sentence ends in . ? !
    # don't count decimals 

    punct = [".", "!", "?"]

    for word in file_words:
        if word[-1] in punct:
            count += 1
    

    if count is 1:
        print("There is one sentence in '{}'".format(a_filename))
    elif count > 1:
        print("There are {c} sentences in '{f}'".format(c=count, f=a_filename))
    else:
        print("There are no sentences in '{}'".format(a_filename))
    
    my_file.close()

    
    
