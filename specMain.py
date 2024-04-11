from specHuman.specHuman import specHuman
from specAI import specAI

filepath = ""

def chooseGameMode():
   print("Choose your game mode:")
   print("1. Human vs Human")
   print("2. Human vs AI")

   while True:
      choice = input("Enter your choice (1 or 2): ")
      if choice in ['1', '2']:
         break
      else:
         print("Invalid choice. Please choose 1 or 2.")

   if choice == '2':
        print("Choose AI difficulty level: easy(1), medium(2), or hard(3)")
        while True:
            difficulty = input("Enter the difficulty level: ")
            if difficulty in ['1', '2', '3']:
                break
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
   else:
       difficulty = None

   return choice, difficulty


choice, difficulty = chooseGameMode()
if choice == '1':
    print("You've chosen Human vs Human mode.")
    specHuman()
else:
    print("You've chosen Human vs AI mode.")
    specAI(difficulty)