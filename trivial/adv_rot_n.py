'''
A less naive implementation of ROT-N. Uses mod instead of addn/subt to norm.

See the rot_n.py header doc.
'''

import string

def rotateLetter(letter, n):
    if letter.isupper():
        newLetter = (chr(ord('A') + ((ord(letter) - ord('A') + n) % 26)))
        return newLetter
    elif letter.islower():
        newLetter = (chr(ord('a') + ((ord(letter) - ord('a') + n) % 26)))
        return newLetter
    else:
        return letter

def rotateWord(word, n):
    result = ''
    for letter in word:
        result += rotateLetter(letter, n)
    return result

if __name__ == '__main__':
    plaintext = raw_input("\nEnter plaintext: ")
    n = int(raw_input("Rotate by how much?: "))
    print "\nHere is the ciphertext: {}\n".format(rotateWord(plaintext, n))
