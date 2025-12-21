# used to store multiple values but immutable (you can't perform add or remove operation)
 
# Ordered -> indexing present
t1 = (1, 2, 3)
print(f"Tuple t1 : {t1}")

# for single element tuple comma is mandatory
t2 = (1,)
print(f"t2 : {t2}")

# tuple elements can be accessed via indexes
t = ("apple", "banana", "cherry")

print(t[0])   # apple
print(t[-1])  # cherry

# Lets test its immutability 
t4 = (1, 2, 3)
# lets try changing value of first element 
try:
    t4[0] = 3
except Exception as e:
    print(f"Following exception occured : {e}")

print(f"t4 : {t4}")

# When do we need list and when do we need tuples 
### Tuples : You want to protect data from modification
### Lists : When you want data to be modified