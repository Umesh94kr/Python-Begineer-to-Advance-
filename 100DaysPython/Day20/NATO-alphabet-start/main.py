# 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import os
import pandas as pd

BASE_DIR = os.path.dirname(__file__)
CSV_PATH = os.path.join(BASE_DIR, 'nato_phonetic_alphabet.csv')


df = pd.read_csv(CSV_PATH)

letters_words = {row.letter : row.code for index, row in df.iterrows()}

# 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("What is your name? ").upper()
result = {alphabet : letters_words[alphabet] for alphabet in user_input}
print(result)

