def shift_cipher(a_string, shift):
    # shift states how many letters each letter should be shifted
    # if shift = 3, then A = D, B = E
   
    end_shift = 26 - shift 
    range_begin = ord('Z') - shift + 1   
    range_end = ord('Z') # z = 90

    converted_list = []
    a_string = a_string.upper()
        
    for char in a_string:
        if char.isalpha():
            if ord(char) in range(range_begin, range_end+1):
                converted_list.append(chr(ord(char) - end_shift+1))
            else:
                converted_list.append(chr(ord(char) + shift))
        else:
            converted_list.append(char)
            
    new_string = ""
    ''.join(converted_list)
    print(''.join(converted_list))
