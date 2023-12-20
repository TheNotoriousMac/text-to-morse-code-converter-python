"""
Text to Morse Code Converter created with basic python...
"""

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}



def translate_to_morse_code(text):
    morse_code = ''
    for letter in text:
        if letter in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[letter] + ' '
    return morse_code

def main():
    print("""
    🅼🅾🆁🅴🆂🅴 🅲🅾🅳🅴 🅲🅾🅽🆅🅴🆁🆃🅴🆁
    """)
    text_input = input("Please enter the text you would like to convert: ")
    text_input = text_input.upper()

    print(translate_to_morse_code(text_input))


if __name__ == "__main__":
    main()
