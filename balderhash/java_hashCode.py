'''
Prompts the user a string and prints its hash code.

Based on the java.lang.String hashCode() method
'''

import string

def hashCode(s):
    hash = 0
    for i in range(len(s)):
        hash = ord(s[i]) + (31 * hash)
    return hash;

if __name__ == '__main__':
    text = raw_input("\nEnter a string: ")
    print "Hash code: {}\n".format(hashCode(text))
