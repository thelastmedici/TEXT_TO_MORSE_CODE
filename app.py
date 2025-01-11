def morse_converter():
    """
        This program provides functionality to convert text to morse code and vice versa.
    """
    

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

    MORSE_CODE_DICT = {**letters, **numbers, **symbols}
    REVERSED_MORSE_DICT = {}
    game_on= True
    for char, morse in MORSE_CODE_DICT.items():
        REVERSED_MORSE_DICT[morse] = char

    def encode_to_morse():
        """A function that converts a string to Morse code."""
        user_text = input("Enter the text you want to convert to Morse code: ").upper()
        morse_code = ""
        for chars in user_text:
            if chars in MORSE_CODE_DICT:
                morse_code += MORSE_CODE_DICT[chars] + " "
            elif chars == " ":
                morse_code += "/ "  # Add a slash for spaces between words
            else:
                return f"Error: You have entered an invalid character: {chars}"

        return f"The Morse code for the given text is: {morse_code.strip()}"


    def decode_from_morse():
        """A function that converts morse codes to text"""
        morse_text = input("Enter the morse code for the given text").strip()
        if not morse_text:
            return "No morse code provided"
        text = ""
        words = morse_text.split(" / ")
        for word in words:
            for morse_code in word.split(" "):
                if morse_code in REVERSED_MORSE_DICT:
                    text += REVERSED_MORSE_DICT[morse_code]
                else:
                    return f"Error: Invalid morse code: {morse_code}"
                text += " "
        return text.strip()
    print("Welcome to my Morse code converter app!\n")
    print("Enter 'Q' to quit at any time.")

    while game_on:
        user_choice = input("TYPE 'E' for encode or 'D' for decode: ").upper()
        if user_choice == 'E':
            print(encode_to_morse())
        elif user_choice == 'D':
            print(decode_from_morse())
        elif user_choice == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.") 

if __name__ == '__main__':
    morse_converter()

        