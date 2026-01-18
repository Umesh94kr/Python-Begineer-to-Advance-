# Can you remove duplicates from a sorted array?

array = [1, 1, 2, 2, 2, 3, 4, 5]

def remove_duplicates(array: list) -> list:
    prev = array[0]
    array_len = len(array)
    i = 1
    for _ in range(1, array_len):
        current = array[i]
        if prev == current:
            prev = array[i]
            array.pop(i-1)
        else:
            prev = array[i]
            i += 1

    return array

print(remove_duplicates(array))