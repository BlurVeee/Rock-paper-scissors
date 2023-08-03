from getpass import getpass as input
print("Welcome to the best Rock paper scissors game 🪨 📄 ✂️")
print()
print("Instead of typing the entire word, only type out the first letter of the move you are choosing")
print()
print("Rock = R or r")
print("Paper = P or p")
print("Scissors = S or s")
print()
print()
counter_1 =+ 0
counter_2 =+ 0

while True:
  player_1 = input("Player 1 : Rock Paper or Scissors?: ")
  player_2 = input("Player 2: Rock Paper or Scissors?: ")
  print()
  if player_1 == "R" or player_1 == "r":
   if player_2 == "R" or player_2 == "r":
    print("IT IS A DRAW")
   elif player_2 == "P" or player_2 == "p":
    print("Paper ate Rock - PLAYER 2 is the winner")
    counter_2 += 1
    print("Player 1 has", counter_1, "point")
    print("player 2 has", counter_2, "point")
   elif player_2 == "S" or player_2 == "s":
    print("Rock smashed scissors - PLAYER 1 WINNNNNNN")
    counter_1 += 1
    print("Player 1 has", counter_1, "point")
    print("player 2 has", counter_2, "point")
   else:
    print("Restart because someone did not play using R, P or S")
    
  elif player_1 == "P" or player_1 == "p":
   if player_2 == "P" or player_2 == "p":
     print("damm a draw")
   elif player_2 == "R" or player_2 == "r":
     print("Paper ate Rock - PLAYER 1 is the winner")
     counter_1 += 1
     print("Player 1 has", counter_1, "point")
     print("player 2 has", counter_2, "point")
   elif player_2 == "S" or player_2 == "s":
     print("Scissors cut paper - PLAYER 2 won the game")
     counter_2 += 1
     print("Player 1 has", counter_1, "point")
     print("player 2 has", counter_2, "point")
   else:
     print("Restart because someone did not play using R, P or S")
    
  elif player_1 == "S" or player_1 == "s":
    if player_2 == "S" or player_2 == "s":
     print("Both of you are loser AHAHAHAH")
    elif player_2 == "P" or player_2 == "p":
     print("Scissors cut paper - PLAYER 1 won the game")
     counter_1 += 1
     print("Player 1 has", counter_1, "point")
     print("player 2 has", counter_2, "point")
    elif player_2 == "R" or player_2 == "r": 
      print("Rock smashed scissors - PLAYER 2 WINNNNNNN")
      counter_2 += 1
      print("Player 1 has", counter_1, "point")
      print("player 2 has", counter_2, "point")
    else:
      print("Restart because someone did not play using R, P or S")

  else:
    print("Restart because someone did not play using R, P or S")
    
  print()
  print()
  print()

  if counter_1 == 3:
    print("PLAYER 1 IS THE ULTIMATE WINNER")
    break
    exit()
  elif counter_2 == 3:
    print("PLAYER 2 IS THE ULTIMATE WINNER")
    break
    exit()
