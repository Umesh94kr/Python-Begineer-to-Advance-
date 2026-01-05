# Data Overlap
# 💪 This exercise is HARD 💪 

# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line. 

# You are going to create a list called result which contains the numbers that are common in both files. 

# e.g. if file1.txt contained: 
# 1 
# 2 
# 3

# and file2.txt contained: 
# 2
# 3
# 4

# result = [2, 3]

###################### SOLUTION ######################
import os 

BASE_DIR = os.path.dirname(__file__)
FILE1 = os.path.join(BASE_DIR, 'file1.txt')
FILE2 = os.path.join(BASE_DIR, 'file2.txt')

l1 = []
with open(FILE1, 'r') as f:
    for line in f:
        l1.append(int(line.rstrip()))

l2 = []
with open(FILE2, 'r') as f:
    for line in f:
        l2.append(int(line.rstrip()))

# common numbers in both the lists
l3 = [num for num in l1 if num in l2]
print(l3)