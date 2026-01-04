import pandas as pd 
import os 

BASE_PATH = os.path.dirname(__file__)
SQIRREL_FILE = os.path.join(BASE_PATH, '2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

df = pd.read_csv(SQIRREL_FILE)
print(f" Columns : {df.columns}")

types_of_fur_color = df['Primary Fur Color'].value_counts()
print(types_of_fur_color)

