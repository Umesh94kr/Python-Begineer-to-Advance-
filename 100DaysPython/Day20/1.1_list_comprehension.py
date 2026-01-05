# List comprehension is a concise Python syntax for creating a new list by transforming or filtering elements from an existing iterable (like a list, range, string, etc.).
# ✅ Shorter and cleaner
# ✅ Often faster than loops
# ✅ More readable (when not overused)

l1 = [1, 2, 3, 4]
# make a new list that contains +1 of numbers in previous list
## Old method
l2 = []
for number in l1:
    l2.append(number+1)
print(l2)

## New method - list comprehension
l3 = [number+1 for number in l1]
print(l3)

## Create a list in which number in the range(1, 5) are doubled
l4 = [2*number for number in range(1, 5)]
print(l4)

## filter out names in new list where length in less than or equals to 4 letters 
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']

l5 = [name for name in names if len(name) <= 4]
print(l5)

## make a new list where names are in uppercase 
l6 = [name.upper() for name in names]
print(l6)