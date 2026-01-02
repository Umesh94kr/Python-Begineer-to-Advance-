# You will be provided by the list of friends, now randomly select a friend who will pay the bill
import random

friends = ['Alice', 'Suzan', 'Mike', 'Jason', 'Vidyut']

total_friends = len(friends)

random_index = random.randint(0, total_friends-1)

print(f"Bill will be paid by : {friends[random_index]}")
