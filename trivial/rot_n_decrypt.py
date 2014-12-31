'''
Prompts the user for ciphertext and prints out all 26 possible rotations of
the ciphertext. [It is then up to the user to decide which one should be the
plaintext.]

TODO: then it searches for an instance of the words in an English words list
(words.txt) and returns the most likely ROT-N used followed by the most likely
plaintext.

Also see the rot_n.py header doc.
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

def getCiphertext():
    plaintext = raw_input("\nEnter ciphertext: ")
    return plaintext

def printPossPlaintexts(ciphertext):
    for i in range(1,26):
        print "ROT-{}: {}".format(i, rotateWord(ciphertext, i))
    print ""

if __name__ == '__main__':
    ciphertext = getCiphertext()
    print "\nHere are the possible plaintexts: "
    printPossPlaintexts(ciphertext)

