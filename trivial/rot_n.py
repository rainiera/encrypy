'''
Prompts the user for plaintext, how much they want to rotate the alphabet by,
and prints out the ciphertext.

normalize() "wraps" the letter back to the beginning of the alphabet, in case its translation exceeds the decimal Unicode mapping for that letter's case.

Also note that
ord(A,Z) = 65, 90
ord(a,z) = 97, 122
as these are the values used as bounds for the normalize() function
'''

import string

def normalize(letter, minimum, maximum):
    if letter > maximum:
        letter -= 26
    elif letter < minimum:
        letter += 26
    return letter

def rotateLetter(letter, n):
    if letter.isupper():
        start = normalize(ord(letter) + n, 65, 90)
    else:
        start = normalize(ord(letter) + n, 97, 122)

    newLetter = chr(start)
    return newLetter

def rotateWord(word, n):
    result = ''
    for letter in word:
        result += rotateLetter(letter, n)
    return result

def getPlaintext():
    plaintext = raw_input("\nEnter plaintext: ")
    return plaintext

def getN():
    n = int(raw_input("Rotate by how much?: "))
    return n

if __name__ == '__main__':
    plaintext = getPlaintext()
    shift = getN()
    print "\nHere is the ciphertext: "
    print rotateWord(plaintext, shift) + "\n"
