# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-
""" 
1. We created a function with the parameters message and shift
2. Create a variable that will hold the encrypted message
3. Create an if statement that if the message is in letters then it will convert the message
4. shiftedval carries the ascii value and adds the shift value
5. the tempchar then converts the ascii value(integer) into a string
6. This string is stored into our empty variable and is then returned
"""

def caesor_ciphor_encryption(msg,shift):

    enc=""
    for char in msg:
        if char.isalpha():
            if char.isupper():
                shiftedval=ord(char)+shift
                if shiftedval>90:
                    a=shiftedval-65
                    a=a+shift
                    a=a%26
                    a+=65
                    tempchar=chr(a)
                    enc+=tempchar
                    print(enc)
                else:
                    shiftedval=ord(char)+shift
                    tempchar=chr(shiftedval)
                    enc+=tempchar
                    print(enc)
            if char.islower():
                shiftedval=ord(char)+shift
                if shiftedval>122:
                    a=shiftedval-97
                    a=a+shift
                    a=a%26
                    a+=97
                    tempchar=chr(a)
                    enc+=tempchar
                    print(enc)
                else:
                    shiftedval=ord(char)+shift
                    tempchar=chr(shiftedval)
                    enc+=tempchar
                    print(enc)
            
    return caesor_ciphor_encryption
caesor_ciphor_encryption("hey reyn",2)

