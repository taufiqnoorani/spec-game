from setupRound import getScorecards, getShowcards

pre = 'Sprint#1/images/cards/card'
sep = '-' 
formt = '.png'

rankMap = {
    "Ace": "1",
    "Two": "2",
    "Three": "3",
    "Four": "4",
    "Five": "5",
    "Six": "6",
    "Seven": "7",
    "Eight": "8",
    "Nine": "9",
    "10": "10",
    "Jack": "11",
    "Queen": "12",
    "King": "13"
}

suiteMap = {
    "Spades": "spades",
    "Hearts": "hearts",
    "Diamonds": "diamonds",
    "Clubs": "clubs"
}

#Input - card, as list element of showcards [Pos, Rank, Suite, Flip?]
#Output - card asset name
def getCardAsset(card):
    if card[1] == "Joker":
        return pre + sep + "blank" + formt
    return pre + sep + suiteMap[card[2]] + sep + str(rankMap[card[1]]) + formt


