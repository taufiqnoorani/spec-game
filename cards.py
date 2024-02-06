import pandas as pd
import random
import pandas as pd
import random

filePath = ""

def scorecards():
            # Read the CSV data into a DataFrame
            scorecardsDf = pd.read_csv(filePath+"scorecards.csv")

            # Sort the DataFrame in descending order by 'Points'
            scorecardsDf = scorecardsDf.sort_values('Points', ascending=False)

            # Convert the DataFrame to a list of lists, reorder columns and eliminate 'Position'
            scorecards = scorecardsDf[['Points', 'Rank', 'Suite']].values.tolist()

            return scorecards


def showcards():
    # Read the CSV data into a DataFrame
    showcardsDf = pd.read_csv(filePath+"showcards.csv")

    # Strip leading/trailing spaces from 'Rank' and 'Suite'
    showcardsDf['Rank'] = showcardsDf['Rank'].str.strip()
    showcardsDf['Suite'] = showcardsDf['Suite'].str.strip()

    # Convert the DataFrame to a list of lists, reorder columns
    showcards = showcardsDf[['Rank', 'Suite']].values.tolist()

    # Shuffle the list
    random.shuffle(showcards)

    # Add 'Position' at index 0
    showcards = [[str(i+1)] + card for i, card in enumerate(showcards)]

    return showcards

scorecardsP = scorecards()
print(f"This is {scorecardsP}")
print("This is a break between the scorecards and the showcards\n\n\n\n\n\n\n")
showcardsP = showcards()
print(f"This is {showcardsP}")