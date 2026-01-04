NAMES_PATH = 'Input/Names/invited_names.txt'
LETTER_PATH = 'Input/Letters/starting_letter.txt'
STORE_LETTER_PATH = 'Output/Ready_to_send'

import os 

BASE_DIR = os.path.dirname(__file__)
NAMES_PATH = os.path.join(BASE_DIR, NAMES_PATH)
LETTER_PATH = os.path.join(BASE_DIR, LETTER_PATH)
STORE_LETTER_PATH = os.path.join(BASE_DIR, STORE_LETTER_PATH)

# function to construct a letter given name and content 
def construct_a_letter(content, name):
    new_letter = content.replace('[name]', name)
    return new_letter



# read the names files and store each name in a list
names = []
with open(NAMES_PATH, 'r') as f:
    for line in f:
        names.append(line.rstrip())
    print(names)

# extract the letter content 
with open(LETTER_PATH, 'r') as f:
    content = f.read()

# Now for each name I want to write a letter and store it 
for name in names:
    letter = construct_a_letter(content, name)
    store_path = os.path.join(STORE_LETTER_PATH, f'letter_to_{name}')
    with open(store_path, 'w') as f:
        f.write(letter)