#Program for encoding and decoding morse code by Kashish Handa
#https://Github.com/kashishh2
#First we will create a morse code dictionary:
morse ={'A':'.-', 'B':'-...',
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

# a function to encrypt to morse code
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '
    return cipher
