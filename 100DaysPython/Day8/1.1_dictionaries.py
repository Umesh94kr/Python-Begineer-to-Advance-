# Python dictionaries allow to store values in key-value pairs, they are mutable 
marks = {'Angela' : 90, 'Jack' : 40, 'Umesh' : 70}

# you can access a value by its key 
print(f"Marks of Angela : {marks['Angela']}")

# check whether a key is present in dictionary or not
if 'Angela' in marks.keys():
    print("Yes")

# adding another record 
marks['Jerry'] = 40
print(marks)

# looping over a dictionary 
for key, value in marks.items():
    print(f"Key -> {key}, Value -> {value}")