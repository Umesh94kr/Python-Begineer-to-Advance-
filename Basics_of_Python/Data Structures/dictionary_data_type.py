# collection of key-value pairs where each key is unique and maps to a value 
dict1 = {
    "name" : "Umesh",
    "designation" : "Data Scientist",
    "age" : 21
}

# its mutable 
dict1['married'] = False
print(dict1)

# accessing values by their keys 
print(dict1['name'])

# removing keys
dict1.pop('name')
print(dict1)

# removing last element 
dict1.popitem()
print(dict1)

# looping through dictionary 
for key, value in dict1.items():
    print(f"Key : {key} -> Value : {value}")

# Dictionary = Unordered, Key-Value, Mutable, Fast lookups