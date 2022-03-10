def affine_cipher(a_string, a, b):

    encrypted_list = []
    a_string = a_string.upper()

    for char in a_string:
        if char.isalpha():
            c = ((a * (ord(char)- 64) + b) % 26)
            if c == 0:
                c = 26
            encrypted_list.append(chr(c + 64))
            
        else:
            encrypted_list.append(char)

    
    encrypted_string = "".join(encrypted_list)

      
    return encrypted_string
