from art import logo

print(logo)
print("Welcome to the secret auction program. ")

still_bidders = True
bids = {}

while still_bidders :
    user_name = input("What is your name? ")
    user_bid = int(input("What's your bide? $"))
    still_bidders = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    if still_bidders == "no":
        still_bidders = False
