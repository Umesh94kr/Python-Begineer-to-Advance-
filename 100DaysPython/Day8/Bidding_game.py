bidder = True 
highest_bid = 0
highest_bidder = ""

while(bidder):
    name = input("Name of Bidder? ")
    amount = int(input("Amount submitted by Bidder? "))

    if amount > highest_bid:
        highest_bid = amount 
        highest_bidder = name
    
    any_bidder = input("Is there any other Bidder? Yes or No - ")
    if any_bidder == 'No':
        bidder = False

print(f"Highest Bid of amount ${highest_bid} is placed by {highest_bidder}.")