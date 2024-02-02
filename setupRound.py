import pandas as pd
import random

#My file path is different for some reason, use which ever works for you
filePath = "spec-game/"
#filePath = ""

#The main file should have this globally declared in the future
#For displaying in the terminal, might be cleaner to show the symbol instead of the text for suites
suiteDict = {"Spade": "♠",
             "Heart": "♥",
             "Club": "♣",
             "Diamond": "♦",
             "Joker": "🃏"}


def getScorecards():
    scorecards = pd.read_csv(filePath+"scorecards.csv")
    return scorecards

def getShowcards():
    showcards = pd.read_csv(filePath+"showcards.csv")
    return showcards

#The Grid is a 5x5 dataframe.
#Each cell is a list containing [Rank,Suit] as a list. eg - [Jack,Heart]
#Paramters - dataframe containing the showcards in no particular order
def generateGrid(showcards):
    #Random unique number list
    randomList = random.sample(range(0,25),25)
    #print(randomList)

    rowList = []
    grid = pd.DataFrame()
    column = 0
    for i in randomList:
        rowList.append([showcards.iloc[i].Rank,showcards.iloc[i].Suite,0])
        column+=1
        if(column==5):
            column=0
            grid = pd.concat([grid, pd.DataFrame([rowList])], ignore_index=True)
            rowList.clear()

    #print(grid)
    grid.to_csv(filePath+"grid.csv")
            

generateGrid(getShowcards())