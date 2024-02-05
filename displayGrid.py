import pandas as pd

full_grid_list = []

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
    global full_grid_list
    for r in range(0,5):
        for c in range(0,5):
            card = grid.iloc[r][c+1]
            cardList = stringToList(card)

            #grid data in a list to use in every round, this data will be used to analyze the grid changes
            full_grid = grid.iloc[r][c + 1]
            full_grid_list .append(stringToList(full_grid))

            #print(full_grid_list)
            if(cardList[2]=="0"):
                #row = row+"   "+cardList[0]+" "+suiteDict.get(cardList[1])
                formattedCard = f"{cardList[0]} {suiteDict.get(cardList[1])}"
                row += f"| {formattedCard:<3} "
            else:
                row = row+" XX "
        print(row)
        row=""
        print("+------+------+------+------+------+")

#TODO: please display this in main and test in main file, becuase when i call this file it displayes uneccesarry data
#TODO: create a separate method just to display becuase i need to call this method everytime i need updated grid, so separate the logic and display part
displayGrid()

#sending the grid in list format
def return_stateful_list():
    return full_grid_list
