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

#[['Ace', 'Spade', '0'], ['10', 'Diamond', '0'], ['Queen', 'Diamond', '0'], ['Queen', 'Spade', '0'], ['2', 'Diamond', '0'], ['Jack', 'Heart', '0'], ['Queen', 'Club', '0'], ['Jack', 'Spade', '0'], ['Ace', 'Diamond', '0'], ['King', 'Spade', '0'], ['King', 'Club', '0'], ['2', 'Spade', '0'], ['Queen', 'Heart', '0'], ['Jack', 'Diamond', '0'], ['2', 'Heart', '0'], ['Joker', 'Joker', '0'], ['10', 'Heart', '0'], ['Ace', 'Heart', '0'], ['King', 'Heart', '0'], ['King', 'Diamond', '0'], ['2', 'Club', '0'], ['Jack', 'Club', '0'], ['10', 'Spade', '0'], ['10', 'Club', '0'], ['Ace', 'Club', '0']]

#TODO: please display this in main and test in main file, becuase when i call this file it displayes uneccesarry data
#TODO: create a separate method just to display becuase i need to call this method everytime i need updated grid, so separate the logic and display part
displayGrid()

#sending the grid in list format
def return_stateful_list():
    return full_grid_list