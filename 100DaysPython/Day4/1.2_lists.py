# List is a Data Structure which is ordered and mutable 
fruits = ['apple', 'banana', 'grapes']

# print all fruits 
print(fruits)

# print first element from fruits 
print(fruits[0])

# print last element from fruits 
print(fruits[-1])

# in lists first element is accessed by '0' and last can be 'len(list)-1'

# appending a new fruit is the list 
fruits.append('cheeku')
print(fruits)

# removing element from specific index 
fruits.pop(-1) # removes last element
print(fruits)

# extend is used to add second list in first one 
sports = ['football', 'badminton', 'squash', 'swimming']

fruits.extend(sports)
print(f"Sports : {sports}")
print(f"Fruits : {fruits}")

# deleting a list 
del fruits[:] 
print(fruits)