import os
import platform

biding = {}

def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def max_bid():
    max_bidder = max(biding, key=biding.get)
    print(f"The highest bid was from {max_bidder} with a bid of ₹{biding[max_bidder]}.")


def entry():
    while True:
        name = input("Enter your name: ")
        bid = int(input("Enter your bid: "))
        biding[name] = bid
        more = input("Are there more people for bid (yes or no): ").lower()
        clear()
        if more != "yes":
            max_bid()
            break
        
        
            

# Start the program
entry()

