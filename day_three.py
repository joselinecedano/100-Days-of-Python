''' 
This is a game called Treasure Island. The player is presented with a series of choices that will lead them to the treasure or to their demise.
'''

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

first_move = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right'\n").lower()
if first_move == "right":
  print("Oh no! You fell into a hole. Game over.")
elif first_move == "left":
  second_move = input("You have come to a lake. There is an island in the middle of the lake. Would you like to swim across or wait for a boat? Type 'swim' or 'wait'\n").lower()
  if second_move == "swim":
    print("Oh no! You were attacked by trout. Game over.")
  elif second_move == "wait":
    third_move = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n").lower()
    if third_move == "red":
      print("Oh no! You were burned by fire. Game over.")
    elif third_move == "blue":
      print("Oh no! You were eaten by beasts. Game over.")
    elif third_move == "yellow":
      print("Yay! You found the treasure! You win!")
    else:
      print("Oh no! You triggered a trap. Game over.")
  else:
    print("Oh no! You were attacked by trout. Game over.")
else:
  print("Oh no! You fell in a hole. Game over.")


# returns the following:
'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************

Welcome to Treasure Island.
Your mission is to find the treasure.
You are at a crossroad. Where do you want to go? Type 'left' or 'right'
left
You have come to a lake. There is an island in the middle of the lake. Would you like to swim across or wait for a boat? Type 'swim' or 'wait'
wait
You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?
yellow
Yay! You found the treasure! You win!
'''



# here is the link to the flow chart for this game: https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload