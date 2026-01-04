# with keyword is used to open files, reading and writing them 
# using 'with' keyword we do not have to remember about closing the file 
import os
BASE_DIR = os.path.dirname(__file__)
FILE_PATH = os.path.join(BASE_DIR, "sample_text.txt")

# open a file and read the content 
with open(FILE_PATH, 'r') as f:
    content = f.read()
    print(content)

# open a file and write the content (this will not add this line to file but update all the content with this)
with open(FILE_PATH, 'w') as f:
    f.write("New text.")

# to add a new line use 'append' mode
with open(FILE_PATH, 'a') as f:
    f.write('\nWe will a new line to this.')

