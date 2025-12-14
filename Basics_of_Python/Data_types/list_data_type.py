# Lists are a built-in data type in Python used to store multiple values
# of different data types. They are ordered (indexing present), mutable, and support indexing.

my_list = [1, 2, "Umesh", -0.01, True]

# length of list
print(f"Length of list : {len(my_list)}")

# we can access elements in list via index 
print(my_list[0])
print(my_list[4])

# what if we want to add something 
my_list.append("Kumar")
print(f"Now length of list : {len(my_list)}")
print(my_list)

# what if we want to remove an element from list at a specific index
my_list.pop(1)
print(my_list)

# extend method in list is used to combine two lists
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]

l1.extend(l2)
print(f"Now l1 becomes : {l1}")
# l2 remains same as l1 is extended
print(f"Now l2 becomes : {l2}")

# checking if a list is empty or not 
empty_list = []
if not empty_list:
    print(f"List is empty")
