#  File: TestCipher.py

#  Description: 

#  Student's Name: Matthew Umana

#  Student's UT EID: msu245

#  Course Name: CS 313E 

#  Unique Number: 50300

#  Date Created: 2/4/20

#  Date Last Modified: 2/7/20


import math

def rail_fence_encode ( strng, key ):
    strng = filter_string(strng)
    cipher = ""
    lst = [""]*key
    counter = 1
    hitmax = False
    # using the key, places each letter of the strng in a diagonal pattern with the depth of the key size
    for i in strng:
        lst[counter-1]+=i
        if counter == key:
            hitmax = True
        if counter == 1:
            hitmax = False
        if hitmax:
            counter-=1
        else:
            counter+=1

    for i in lst:
        cipher+=i
        
    return filter_string(cipher)


def read_list(lst, key, length):
    dec_str = ""
    counter = 1
    hitmax = False
    col = 0
    
    for j in range(length):   
        dec_str += lst[counter-1][col]
            
        if counter == key:
            hitmax = True
        if counter == 1:
            hitmax = False
        if hitmax:
            counter-=1
        else:
            counter+=1
        col += 1
          
    return dec_str

# decodes a string by reconstructing a 2D list given a key and returns the decoded string
def rail_fence_decode (strng, key):
    lst = [] #makes 2D list
    for i in range(key):
        lst.append([" "]*len(strng))
        
    counter = 1
    hitmax = False
    col = 0
    for i in strng:
            
        lst[counter-1][col] = 0
            
        if counter == key:
            hitmax = True
        if counter == 1:
            hitmax = False
        if hitmax:
            counter-=1
        else:
            counter+=1
        col += 1
        
    index_strng = 0
    
    for i in range(len(lst)):
        for j in range(len(strng)):
            if lst[i][j] == 0:
               lst[i][j] = strng[index_strng]
               index_strng += 1

    dec_str = ""
    counter = 1
    hitmax = False
    col = 0
    
    for i in strng:
            
        dec_str += lst[counter-1][col]
            
        if counter == key:
            hitmax = True
        if counter == 1:
            hitmax = False
        if hitmax:
            counter-=1
        else:
            counter+=1
        col += 1

    return dec_str

# removes all characters in a string that are not letters
def filter_string (strng):
    new_strng = "" 
    for i in strng:
        if i.isalpha():
            new_strng += i
    new_strng = new_strng.lower()
    return new_strng

# encodes a character given the phrase char (p) and the char itself (s)
def encode_character (p, s):
    num_val = get_let_val(p) + get_let_val(s)
    
    if num_val > 25:
        num_val -= 25
        return get_index(num_val-1)
    else:
        return get_index(num_val)
    
# Decodes a character given the phrase char (p) and the char itself (s)
def decode_character (p, s):
    if get_let_val(p) > get_let_val(s):
        num_val = (26-get_let_val(p)) + get_let_val(s)
    else:
        num_val = get_let_val(s) - get_let_val(p)

    if num_val < 0:
        num_val = 25 + num_val
        return get_index(num_val-1)
    else:
        return get_index(num_val)	

# returns the ascii value of a given letter
def get_let_val(strng):
    letter_lst = []
    
    for i in range(97, 123):
        letter_lst.append(chr(i))

    return letter_lst.index(strng)

# returns the letter of a given number/index
def get_index(num):
    letter_lst = []
    
    for i in range(97, 123):
        letter_lst.append(chr(i))

    return letter_lst[num]

# encodes a string using a phrase
def vigenere_encode (strng, phrase):
    strng = filter_string(strng)
    phrase_str = get_phrase_str(strng, phrase)
    cipher_str = ""
    counter = 0
    for i in strng:
        enc_chr = encode_character(i, phrase_str[counter])
        counter += 1
        cipher_str += enc_chr

    return cipher_str

# uses the sizes of the strng and phrase to make the phrase the same length as the strng and returns the extended phrase
def get_phrase_str(strng, phrase):
    num_phrase = math.ceil(len(strng) / len(phrase))
    phrase_str = phrase * num_phrase
    phrase_str = phrase_str[:len(strng)]
    return filter_string(phrase_str)

# decodes a string given a phrase
def vigenere_decode(strng, phrase):
    strng = filter_string(strng)
    phrase_str = get_phrase_str(strng, phrase)
    cipher_str = ""
    cipher = []
    counter = 0
    
    for i in strng:
        enc_chr = decode_character(phrase_str[counter], i)
        cipher_str += enc_chr
        counter += 1

    return cipher_str

def main():
    print("Rail Fence Cipher")
   
  # prompt the user to enter plain text
    plain_text=input("\nEnter Plain Text: ")
    
  # prompt the user to enter the key
    key=int(input("Enter Key: "))

  # encrypt and print the plain text using rail fence cipher
    print("Encoded Text: ",rail_fence_encode(plain_text,key))

  # prompt the user to enter encoded text
    plain_text=input("\nEnter encoded Text: ")
   
  # prompt the user to enter the key
    key=int(input("Enter Key: "))

  # decrypt and print the encoded text using rail fence cipher
  
    print("Decoded Text: ",rail_fence_decode(plain_text,key))

    print("\nVigenere Cipher")

  # prompt the user to enter plain text
    plain_text=input("\nEnter Plain Text: ")

  # prompt the user to enter pass phrase
    pass_phrase=input("Enter Pass Phrase (no spaces allowed): ")
  

  # encrypt and print the plain text using Vigenere cipher
    print('Encoded Text:',vigenere_encode(plain_text,pass_phrase))
    

  # prompt the user to enter encoded text
    plain_text=input("\nEnter Encoded Text: ")

  # prompt the user to enter pass phrase
    pass_phrase=input("Enter Pass Phrase (no spaces allowed): ")

  # decrypt and print the encoded text using Vigenere cipher
    print("Decoded Text:",vigenere_decode(plain_text,pass_phrase))
    
# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
