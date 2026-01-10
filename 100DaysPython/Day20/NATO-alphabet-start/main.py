# 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import os
import pandas as pd

BASE_DIR = os.path.dirname(__file__)
CSV_PATH = os.path.join(BASE_DIR, 'nato_phonetic_alphabet.csv')

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

df = pd.read_csv(CSV_PATH)

letters_words = {row.letter : row.code for index, row in df.iterrows()}

# 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("What is your name? ").upper()

is_done = False
while(is_done == False):
    try:
        result = {alphabet : letters_words[alphabet] for alphabet in user_input}
        is_done = True
    except KeyError as e:
        print(f"Key not exists : {e}")
        print(f"Input name should contain letters")
        user_input = input("What is your name? ").upper()
        is_done=False

print(result)

