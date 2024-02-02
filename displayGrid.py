import pandas as pd

#file_path = "spec-game/"
file_path = "";

suiteDict = {"Spade": "♠",
             "Heart": "♥",
             "Club": "♣",
             "Diamond": "♦",
             "Joker": "🃏"}

#This method converts a string "['1', '2', '3', ...]" to a list ['1,'2','3']
#This is needed because fetching a cell/element of a dataframe fetches it as a string
def stringToList(cell):
    cell = cell.replace("[","")
    cell = cell.replace("'","")
    cell = cell.replace(" ","")
    cell = cell.replace("]","")
    cell = cell.replace("\"","")
    return list(cell.split(","))

def displayGrid():
    grid = pd.read_csv(file_path+"grid.csv")
    row = ""
    for r in range(0,5):
        for c in range(0,5):
            card = grid.iloc[r][c+1]
            cardList = stringToList(card)
            if(cardList[2]=="0"):
                #row = row+"   "+cardList[0]+" "+suiteDict.get(cardList[1])
                formatted_card = f"{cardList[0]} {suiteDict.get(cardList[1])}"
                row += f"| {formatted_card:<3} "
            else:
                row = row+" XX "
        print(row)
        row=""
        print("+------+------+------+------+------+")

displayGrid()