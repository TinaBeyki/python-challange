import os

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    winner = ""
    highest_bid = 0
    for bidder in bids:
        bid_amount = bidding_record[bidder]
        highest_bid = max(bid_amount, highest_bid)
        winner = bidder
    print(f"The winner is {winner} with bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?  ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are ther any other bidders? Type 'yes' or 'no'.")
    os.system('clear')
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)


