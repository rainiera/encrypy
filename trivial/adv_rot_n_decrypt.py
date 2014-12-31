'''
A less naive implementation of rot_n_decrypt.py.
Uses mod instead of addn/subt to account for (char + n) operations
that exceed the decimal Unicode range of that character's case.

Also see the rot_n.py and rot_n_decrypt.py header docs.
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

def printPlaintexts(ciphertext):
    for i in range(1,26):
        print "ROT-{}: {}".format(i, rotateWord(ciphertext, i))
    print ""

if __name__ == '__main__':
    ciphertext = raw_input("\nEnter ciphertext: ")
    print "\nHere are the possible plaintexts: "
    printPlaintexts(ciphertext)
