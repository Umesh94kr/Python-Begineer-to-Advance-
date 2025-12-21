# Unordered collection of unique items
s1 = set()

s1.add(1)
s1.add(2)

print(s1)

# Lets try to add a duplicate value 
s1.add(1)
print(s1)
# it always keep unique values, no duplicates allowed

# checking if a value exists in set
value = 2
if value in s1:
    print(f"This value is present in set")
else:
    print(f"The value is not present in set.")

# removing element if present and giving error if not
try:
    s1.remove(2)
except Exception as e:
    print(f"Error ocuured : {e}")

# more safest way. to remove element without getting an error if not present
s1.discard(3)