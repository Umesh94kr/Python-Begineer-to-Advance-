# find the highest score out of these

marks = [
    78, 85, 92, 67, 88, 74, 90, 81, 69, 95,
    76, 84, 91, 73, 87, 68, 89, 80, 72, 94,
    77, 83, 90, 71, 86, 66, 88, 82, 70, 93,
    75, 84, 92, 69, 87, 74, 91, 79, 68, 96,
    78, 85, 89, 72, 90, 76, 88, 81, 70, 94
]

highest_score = -1

for mark in marks:
    if mark > highest_score:
        highest_score = mark 

print(f"Highest Score is : {highest_score}")

