import pandas as pd
from specAI.setupRound import getShowcards
import textwrap

full_grid_list = []

#file_path = "spec-game/"
filepath = ""

suiteDict = {"SPADES": "♠",
             "HEARTS": "♥",
             "CLUBS": "♣",
             "DIAMONDS": "♦",
             "JOKER": "🃏"}

#This method converts a string "['1', '2', '3', ...]" to a list ['1,'2','3']
#This is needed because fetching a cell/element of a dataframe fetches it as a string
def stringToList(cell):
    cell = cell.replace("[","")
    cell = cell.replace("'","")
    cell = cell.replace(" ","")
    cell = cell.replace("]","")
    cell = cell.replace("\"","")
    return list(cell.split(","))


#[['Ace', 'Spade', '0'], ['10', 'Diamond', '0'], ['Queen', 'Diamond', '0'], ['Queen', 'Spade', '0'], ['2', 'Diamond', '0'], ['Jack', 'Heart', '0'], ['Queen', 'Club', '0'], ['Jack', 'Spade', '0'], ['Ace', 'Diamond', '0'], ['King', 'Spade', '0'], ['King', 'Club', '0'], ['2', 'Spade', '0'], ['Queen', 'Heart', '0'], ['Jack', 'Diamond', '0'], ['2', 'Heart', '0'], ['Joker', 'Joker', '0'], ['10', 'Heart', '0'], ['Ace', 'Heart', '0'], ['King', 'Heart', '0'], ['King', 'Diamond', '0'], ['2', 'Club', '0'], ['Jack', 'Club', '0'], ['10', 'Spade', '0'], ['10', 'Club', '0'], ['Ace', 'Club', '0']]

#TODO: please display this in main and test in main file, becuase when i call this file it displayes uneccesarry data
#TODO: create a separate method just to display becuase i need to call this method everytime i need updated grid, so separate the logic and display part

#sending the grid in list format
def return_stateful_list():
    return full_grid_list


#Display grid from a list of list
#Call this after every turn
def displayGridList(showcards):
    i = 0
    print()
    for r in range(0,5):
        row = ""
        rownum = ""
        for c in range(0,5):
            cardList = showcards[i]
            i+=1
            if(str(cardList[3])=="1"):
                #formattedCard = f"{cardList[1]} {suiteDict.get(cardList[2])}"  
                #row += f"| {formattedCard:<3} "
                if str(cardList[1]).upper() == "JOKER":
                       if str(cardList[2].upper()) != "JOKER":
                            cardList[1] = '2' 
                cardStr = str(cardList[1]).rjust(6,' ') + " " + str(suiteDict.get(cardList[2].upper()))
                #row += cardStr.center(10,' ')
                row += cardStr.ljust(10,' ')
                
                
            else:
                row = row+"XX".center(10,' ')
            numstr = str(cardList[0]).center(10,' ')
            rownum += numstr.center(10,' ')
        print(row)
        print(rownum)
        print()
        print()
        row=""
        rownum=""
        #print("+----------+----------+----------+----------+----------+")

    print()