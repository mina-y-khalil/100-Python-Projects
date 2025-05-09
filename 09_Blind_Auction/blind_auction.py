from art import logo

print(logo)
print("Welcome to the secret auction program. ")

continue_bidding = True
bids = {}

while continue_bidding :
    #Ask the user for input
    user_name = input("What is your name?: ")
    user_bid = int(input("What's your bid? $"))

    #save the input data to dictionary
    bids[user_name] = user_bid

    should_continue = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    if should_continue == "no":
        continue_bidding = False
        def find_highest_bidder(bidding_dictionary):
            winner = ""
            highest_bid = 0
            for bidder in bidding_dictionary:
                bid_amount = bidding_dictionary[bidder]
                if bid_amount > highest_bid:
                    highest_bid = bid_amount
                    winner = bidder
            print(f"The winner is {winner} with a bid of ${highest_bid}.")

        print(find_highest_bidder(bids§))


