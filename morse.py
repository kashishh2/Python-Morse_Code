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
            cipher += morse[letter] + ' '
        else:
            cipher += ' '
    return cipher

# a function to decrypt the morse code
def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2 :
                decipher += ' '
            else:
                decipher += list(morse.keys())[list(morse
                .values()).index(citext)]
                citext = ''
    return decipher

if __name__ == '__main__':
    print("\n Welcome to morse code translations \n Please select one function: \n 1. Encrypt to morse code \n 2. Decrypt to morse code")
    opt = int(input("Enter your choice:"))
    if opt == 1:
        enc = str(input("Enter the String to be translated:"))
        print("The morse code translation is :")
        print(encrypt(enc))
    elif opt == 2:
        enc = str(input("Enter the string to be decripted:"))
        print("The morse code translation is :")
        print(decrypt(enc))
    else:
        print("Wrong option")
        
