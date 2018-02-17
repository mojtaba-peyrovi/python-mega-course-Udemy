import string, random
vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'
all_letters = string.ascii_lowercase
letter_input_1 = input("wht letter do  you want? enter'v' for vowel, 'c' for consonant, and 'l' for any letter: ")
letter_input_2 = input("wht letter do  you want? enter'v' for vowel, 'c' for consonant, and 'l' for any letter: ")
letter_input_3 = input("wht letter do  you want? enter'v' for vowel, 'c' for consonant, and 'l' for any letter: ")


def generator():
    #letter_input_1
    if letter_input_1 == 'v':
        letter1 = random.choice(vowels)
    elif letter_input_1 =='c':
        letter1 = random.choice(consonants)
    elif letter_input_1 =='l':
        letter1 = random.choice(all_letters)
    else:
        letter1 = letter_input_1

    #letter_input_2
    if letter_input_2 == 'v':
        letter2 = random.choice(vowels)
    elif letter_input_2 =='c':
        letter2 = random.choice(consonants)
    elif letter_input_2 =='l':
        letter2 = random.choice(all_letters)
    else:
        letter2 = letter_input_2

    #letter_input_3
    if letter_input_3 == 'v':
        letter3 = random.choice(vowels)
    elif letter_input_3 =='c':
        letter3 = random.choice(consonants)
    elif letter_input_3 =='l':
        letter3 = random.choice(all_letters)
    else:
        letter3 = letter_input_3

    name = letter1 + letter2 + letter3
    return(name)


for x in range(20):
    print(generator())
