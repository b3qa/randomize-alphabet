import string
import random

def randomize_alphabet():
    characters = string.ascii_letters + string.digits
    lst = list(characters)
    random.shuffle(lst)

    return ''.join(lst)

if __name__ == '__main__':
    print('Your random alphabet: {}'.format(randomize_alphabet()))