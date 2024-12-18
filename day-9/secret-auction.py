from turtle import clear
bidFinish=False
emptyDictionary={}
def bidRecord(bidding):
    highest=0
    text=""
    for biding in bidding:
        amount=bidding[biding]
        if amount>highest:
            highest=amount
            text=biding
    print(f"the winneer is {text} with bid of ${highest}")   
        
while not bidFinish:
    name=input('what is your name? ')
    bid=int(input('enter your Bid price? $'))
    emptyDictionary[name]=bid
    question=input('is there other person with you who want to bid? type "yes" or "no" ').lower()
    if question=='no':
        bidFinish=True
        bidRecord(emptyDictionary)
    elif question=='yes':
         clear() 
    else:
        print('incorrect answer!')