import itertools
import sys

threshold = 25  # see english_score()

def generate_keys(characters, key_length):
    ''' Generate all permutations of a key of length 3 comprised only of lowercase letters.

    :param   characters: possible letters the key consists of
    :param   key_length: fixed length of the key
    :return: list of triples, ex: [('a', 'b', 'c'), ('a', 'c', 'b') ...]
    '''
    return itertools.permutations(characters, r=key_length)



def xor(data, key):
    ''' XOR all characters of the data one-by-one and build a string.
        Uses chr() and ord() heavily to go from bytes to ASCII and ASCII to
        bytes, respectively.

    :param data: the cipher
    :param key:  the current key
    :return:     the resulting string when the key is applied to each character
    '''

    key = [ord(c) for c in key]    # The key is in lower case letters; convert to bytes
    li = zip(data, itertools.cycle(key))    # 'zip' the cipher characters and the key (cycled over and over) together

    # print li # You kind've have to see this printed out to understand the zip()

    result = ""

    for x, y in li:
        result += chr(x ^ y)    # The actual XORing and string building

    return result


def english_score(text, wordlist):
    ''' Determine how likely a decryption is to be the correct one by how many English words
        it seems to have.

    :param text: the decryption
    :param wordlist: a list of words found in a real dictionary, no definitions
    :return: how many English words the decryption contains
    '''

    score = 0

    if 'the' in text:    # If it doesn't contain 'the', don't even bother searching the dictionary
        for word in text.split():    # iterate by word, i.e. whitespace in the string
            if word in wordlist:
                score += 1
                if score >= threshold:    # Realistically, if you have 25 English words -> likely the right
                                          # decryption, so don't bother doing more costly searches
                    return score
    else:
        return 0

    return score


def sum_ascii_vals(text):
    ''' Required by the problem.

    :return: the sum of the ASCII values
    '''

    sum = 0

    for char in text:
        sum += ord(char)

    return sum

########################################################################################################################


f = open('p059_cipher.txt', 'r')    # Read the cipher into a variable
bytes = map(lambda x: int(x), f.read().split(","))    # Make into a list of 'bytes'

key_permutations = generate_keys("abcdefghijklmnopqrstuvwxyz", 3)    # Generate all possible keys

wordlist = open("/usr/share/dict/american-english", 'r').read().split('\n') # I'm an OED man myself

scores = []
decrypts = {}    # Hash table ('dictionary') where (Key: Score, Value: Encryption key)


print "CIPHER:\n------------------------------"

for i in bytes:    # Hack to print the cipher without newlines after each character
    print i,
else:
    print

print "\nApplying 17576 unique keys to cipher . . . "

# Main loop where we brute force keys and get an answer
for key in list(key_permutations):
    text = xor(bytes, key)
    score = english_score(text, wordlist)
    decrypts[score] = key    # Build a hash table where (Key: Score, Value: Encryption key)
    if score >= threshold:
        break

correct_key = decrypts[max(decrypts, key=lambda i: decrypts[i])]    # search dictionary for largest score and return associated key
plaintext = xor(bytes, correct_key)

print "\nKEY: " + "".join(correct_key) # make key a string with join()
print "\nDECRYPTED MESSAGE:\n------------------------------\n" + plaintext +"\n"

print "Sum of ASCII values: " + str(sum_ascii_vals(plaintext))