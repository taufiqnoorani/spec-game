import pandas as pd
import random

#My file path is different for some reason, use which ever works for you
#filePath = "spec-game/"
filePath = ""

#The main file should have this globally declared in the future
#For displaying in the terminal, might be cleaner to show the symbol instead of the text for suites
suiteDict = {"Spade": "♠",
             "Heart": "♥",
             "Club": "♣",
             "Diamond": "♦",
             "Joker": "🃏"}


#It is still using a CSV to fetch only.
#This can be changed to be statically typed in the future, if there any more changes to the format of the data, CSV is easier to edit
#RETURNS a list of list containing all the scorecards
#[[Points, Rank, Suite], [Points, Rank, Suite], ...]
def getScorecards():
    scorecardList = []
    scorecards = pd.read_csv(filePath+"scorecards.csv")
    for index, row in scorecards.iterrows():
        sc = [str(row["Points"]),str(row["Rank"]),str(row["Suite"])]
        scorecardList.append(sc) 
    return scorecardList



##############  USE THIS TO GET A GRID LIST   ##############
#Returns a randomized list of list containing all the showcards
#[[1, Rank, Suite, 0], [2, Rank, Suite, 0], [3, Rank, Suite, 0] ... [25, Rank, Suite, 0]]
def getShowcards():
    showcardList = []
    randomList = random.sample(range(0,25),25)
    showcards = pd.read_csv(filePath+"showcards.csv")
    i = 1
    for r in randomList:
        sc = [str(i), str(showcards.iloc[r].Rank), str(showcards.iloc[r].Suite), "0"]
        showcardList.append(sc)
        i+=1
    return showcardList




###########################################################################
#I am leaving this method for now. Use getShowcards() to get the gird list#
###########################################################################

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
