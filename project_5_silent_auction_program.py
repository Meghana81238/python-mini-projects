import os 

def find_winner(bidder_data):
    highest_bid=0
    winner=""
    for bidder in bidder_data:
        bid=bidder_data[bidder]
        if bid>highest_bid:
            highest_bid=bid
            winner=bidder
    print(f"the winner is {winner} with a bid price of {highest_bid}")        
    #print(highest_bid)

bidder_data={}


end_of_bidding=False

while not end_of_bidding:
    name=input("what is your name?:")
    price=int(input("what is your bid?:"))
    bidder_data[name]=price
    more_bidders=input("are there more bidders?type 'yes' or 'no':").lower()
    print(bidder_data)
    if more_bidders=="no":
        end_of_bidding=True
        find_winner(bidder_data)
    elif more_bidders=="yes":
        os.system('cls')


