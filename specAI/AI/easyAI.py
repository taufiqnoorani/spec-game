from analyseGrid import analyseGrid, updatedGrid
import random

filepath = ""



# The AI will choose a card at random
def gameAI(showcards):
   cards = []
   for card in showcards:
         if card[3] == '0':  # If the card is unflipped
            cards.append(card)

   # If there are no unflipped cards, return None
   if not cards:
        return None

   rank = ['A', 'K', 'Q', 'J', '10']
   suit = ['H', 'D', 'C', 'S']

   guess = []
   position = random.choice(cards)
   position = position[0]
   rank = random.choice(rank)
   suit = random.choice(suit)

   guess = [position, rank, suit, 0]
   
   return guess