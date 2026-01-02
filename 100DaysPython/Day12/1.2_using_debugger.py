# import pdb 
# add 'pdb.set_trace()' before or after the line of code where you want to temporarily stop execuption of code to check whether everything is fine or not
import pdb
import string

def preprocess_text(text):
    # remove punctuation
    for character in string.punctuation:
        text = text.replace(character, '')

    # add breakpoint 
    pdb.set_trace()

    # split by words 
    words = text.split(' ')
    return words

# call this function
print(preprocess_text("Hey, What are you doing? Are you all right or doing okay!"))

# to stop the debugger you can use : "quit"
# to continue the process you can use : "continue"