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
# ask for what user wants to do
user_choice = input("TYPE 'E' for encode or 'D' for decode: ").upper()
if user_choice == "E":
   user_text = input("Enter the text you want to convert to morse code: ").upper()
   morse_code = " "
   for char in user_text:
       if char in MORSE_CODE_DICT:
           morse_code += MORSE_CODE_DICT[char] + " "
       elif " " in user_text:
           morse_code += "/ "
        
       else:
           print(f"Error you have entered an invalid character: {char}")

    