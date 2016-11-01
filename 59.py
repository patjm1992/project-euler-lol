import itertools

threshold = 25

def sum_ascii_vals():
    ''' This is asked for as part of the answer. '''
    return sum

def assert_contains_english(text):
    ''' If the result of an xor(data, key) contains 'the', it's worth checking out. '''

    if 'the' in text:
        return True
    else:
        return False # probably not english


def xor(data, key):
    '''

    :param data:
    :param key:
    :return:
    '''
    # chr(integer): bytes --> ascii
    # ord(character): ascii --> bytes

    key = [ord(c) for c in key]             # The key is in lower case letters; convert to bytes
    li = zip(data, itertools.cycle(key))

    result = ""

    for x, y in li:
        result += chr(x ^ y)

    return result

def generate_keys(characters, key_length):
    '''

    :param characters:
    :param key_length:
    :return:
    '''
    return itertools.permutations(characters, r=key_length)



# Read file into a list
f = open('p059_cipher.txt', 'r')


bytes = map(lambda x: int(x), f.read().split(","))

# Convert bytes to ASCII
ascii = [chr(int(c)) for c in bytes]


key_permutations = generate_keys("abcdefghijklmnopqrstuvwxyz", 3)



wordlist = open("/usr/share/dict/american-english", 'r').read().split('\n')



def english_score(text, wordlist):

    score = 0


    # If it doesn't have 'the' don't waste time searching a dictionary

    if 'the' in text:
        for word in text.split():  # iterate by word, i.e. whitespace in the string
            if word in wordlist:
                score += 1
                if score >= 25:
                    print score
                    return score
    else:
        return 0

    print score
    return score



# Main loop where we brute force keys
scores = []
decrypts = {}
for key in list(key_permutations):

    text = xor(bytes, key)
    score = english_score(text, wordlist)

    decrypts[score] = key
    if score >= 25:
        break

correct_key = decrypts[max(decrypts, key=lambda i: decrypts[i])]       # search dictionary for largest score and return associated key
plaintext = xor(bytes, correct_key)

print "KEY: " + "".join(correct_key) # make key a string with join()
print "\nDECRYPTED MESSAGE: \n------------------\n" + plaintext +"\n"
