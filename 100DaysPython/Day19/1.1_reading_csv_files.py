import os 

BASE_PATH = os.path.dirname(__file__)
DATA_FILE = os.path.join(BASE_PATH, 'weather_data.csv')

# reading using with 
with open(DATA_FILE, 'r') as f:
    data = f.readlines()
    print(data)

# reding using csv
import csv 
with open(DATA_FILE, 'r') as f:
    data = csv.reader(f)
    for row in data:
        print(row)
        print('-'*65)

# reading csv file using pandas - Python Data Analysis library
import pandas as pd 
df = pd.read_csv(DATA_FILE)
temperatures = df['temp']
print(temperatures)

# converting pandas dataframe to dictionary 
data_dict = df.to_dict()
print(data_dict)

# getting data of a particular row 
print("Monday Temperature", df.iloc[0][1])