"""
     This program provides functionality to convert text to morse code and vice versa.
 """
print("Welcome to my Morse code converter app!\n")

# create a dictionary for morse code
letters = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..'}
numbers = {'1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}

symbols = {'.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--',
            '/': '-..-.', '()': '-.--.-',
            '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
            '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
            '$': '...-..-', '@': '.--.-.'}
# function to encode
# 

 #function to decode
 # #def decode_from_morse():

MORSE_CODE_DICT = {**letters, **numbers, **symbols}
# # ask for what user wants to do
# def encode_to_morse():
#     """A function that converts a string to morse code"""

#     user_choice = input("TYPE 'E' for encode or 'D' for decode: ").upper()
#     if user_choice == "E":
#         user_text = input("Enter the text you want to convert to morse code: ").upper()
#         morse_code = " "
#         for char in user_text:
#             if char in MORSE_CODE_DICT:
#                 morse_code += MORSE_CODE_DICT[char] + " "
#             elif " " in user_text:
#                 morse_code += "/ "
#             else:
#                 return f"Error you have entered an invalid character: {char}"

#     return f"The morse code for the given text is: {morse_code.strip()}"


#Reversal of morse_code dictionary from the original dictionary
REVERSED_MORSE_DICT = {}
for char, morse in MORSE_CODE_DICT.items():
    REVERSED_MORSE_DICT[morse] = char
print(REVERSED_MORSE_DICT)
##loop througn each key value pair in the original dictionary
##Add the Morse code (value) as the key in the new dictionary.
##Add the character (key) as the value in the new dictionary.


# if user_choice == "D":
#    user_text = input("Enter the morse code you want to convert to text: ")
#    user_text += " "
#    text = ""
#    code = ""
#    for char in user_text:
#        if char != " ":
#            i = 0
#            code += char
#        else:
#            i += 1
#            if i == 2:
#                text += " "
#            else:
#                text += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(code)]
#                code = ""
#    print(f"The text for the given morse code is: {text}")

    