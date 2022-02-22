# CS 232 Spring 2022 Assignment #2
# Sarah Jimenez
# Last modified: February 20, 2022

# Problem 1

# letter_freq: string -> dict
# purpose: expects a string sentence and returns a dictionary with
#          the lowercase letters as keys and the quantity of each
#          letter as values
# side effects: none
# assumptions: the sentence only contains letters and spaces, no punctuation

def letter_freq(sentence):

    sentence = sentence.lower()
    letter_dict = {}

    for char in sentence:
        letter_dict.update({char : sentence.count(char)})

    return letter_dict



# Problem 2

# freq_bar_chart: dict {char : int} -> void
# purpose: to take a dictionary of letters and their frequencies and print
#          a nice-looking bar chart
# side effects: prints a bar chart of the frequencies
# assumptions: the dictionary only has letters that were in the original sentence

def freq_bar_chart(freq_dict):

    sort = sorted(freq_dict.keys())
    
    print("Letter frequency chart:")
    
    for entry in sort:
        print(entry, " - ", "X"*freq_dict[entry])
   


# Problem 3

# plot_points: dict {char : (int, int)} -> void
# purpose: to take in a dictionary of letters and their x,y coordinates and
#          graph them in a 2D list
# side effects: prints a graph to the screen
# assumptions: use the provided supporting function

# max_coordinate_value: dict int -> int
# Expects a dictionary of letters and ordered pairs,
#     and an index value
# Returns the maximum value of the X coordinates if
#     the index value is 0, and the maximum value of
#     the Y coordinates if the index value is 1

def max_coordinate_value(the_dict, the_index):
    max_val = 0
    for a_point in the_dict:
        the_ordered_pair = the_dict[a_point]
        # max_val will have the largest value found so far
        if max_val < the_ordered_pair[the_index]:
            max_val = the_ordered_pair[the_index]
            
    return max_val


def plot_points(the_dictionary):
    # this function works by starting with a single long list
    # that the letters are inserted into and then the
    # list is split into sublists and printed line by line
    
    max_x = max_coordinate_value(the_dictionary, 0)+1
    max_y = max_coordinate_value(the_dictionary, 1)+1

    the_list = []

    # filling a blank lists with .'s
    for i in range(0, (max_x*max_y)):
        the_list.append('.')

    max_y -= 1 # this was needed to make the index equation work

    for letter in the_dictionary:
        x = the_dictionary[letter][0]
        y = the_dictionary[letter][1]
        index = max_x * (max_y - y) + x
        the_list[index] = letter

    the_list = [the_list[i : i + max_x] for i in range(0, len(the_list), max_x)]

    for row in the_list:
        print(row)



# Problem 4
# encode_message: string, int -> list
# purpose: works with the function create_code_ring to take in a string and a
#          seed number, which is then used to generate a list of numbers
#          that correspond to each letter of the string
# side effects: prints to the screen if a non-letter was encountered, so that
#               it doesn't get encoded, and its value is set to 99999
# assumptions: use the provided supporting function to generate the list

# decode_message: list int -> string
# purpose: after encoding a message with encode_message, the code is
#          converted back to a string
# side effects: the string is returned, with '@' added for non-letter characters
# assumptions: letter case isn't preserved; the returned string is all caps

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ-. "

# relative_prime: int int -> bool
# Expects two positive integers >= 2
# Returns True if the integers are relatively prime
#     (that is, is their Greatest Common Divisior is 1)
# DO NOT ALTER THIS CODE!

def relative_prime(num_1, num_2):
    a, b = num_1, num_2
    while (b > 0):
        gcd = b
        b = a % b
        a = gcd
    return gcd == 1
    
# create_code_ring: int -> dict
# Expects a "seed" integer to initialize code mapping
# Returns a dictionary that maps each character in the
#     string constant ALPHABET to an int from 1 to the
#     length of the alphabet
# DO NOT ALTER THIS CODE!

def create_code_ring(seed):
    '''Expects an integer
       Returns a dictionary mapping each letter of a string
       constant ALPHABET to an integer from 1 to len(ALPHABET)'''
    alphabet_len = len(ALPHABET)
    
    # Use seed to set a usable (relatively prime) increment value
    inc_val = seed % alphabet_len
    if inc_val <= 1:
        inc_val = 2
    while not relative_prime(inc_val, alphabet_len):
        inc_val += 1

    # Inititalize index value and code_ring dictionary
    cur_idx = alphabet_len - 1
    code_ring = {}

    for i in list(ALPHABET):
        # Set next index value for mapping
        next_idx = (cur_idx + inc_val) % alphabet_len
        # print(i, " ", next_idx + 1) # UNCOMMENT TO SEE MAPPING
        code_ring.update({ i : next_idx + 1 })
        cur_idx = next_idx
    return code_ring


def encode_message(the_string, seed):
    int_list = []
    code_ring = create_code_ring(seed)

    the_string = the_string.upper()

    for char in the_string:
        if char not in code_ring:
            print('Character {} not encoded, set to 99999'.format(char))
            int_list.append(99999)
            continue
        int_list.append(code_ring.get(char))

    return int_list


def decode_message(the_code, seed):
    original_dict = create_code_ring(seed)
    inverse_dict = {a_value: a_key for a_key, a_value in original_dict.items()}
    
    the_string = ''

    for num in the_code:
        if num not in inverse_dict:
            the_string += '@'
            continue
        the_string += inverse_dict.get(num)

    return the_string 
