import random

options = ("piedra", "papel", "tijera")
rounds = 1 
computer_wins = 0
users_wins = 0

while True:
  print("*"*50)
  print("round", rounds)
  print("*"*50)
  if rounds > 1:
    print("computer_wins", computer_wins)
    print("user_wins", users_wins)
    print("-"*50)

  user_option= input("elija piedra, papel o tijera -> ")
  user_option = user_option.lower()
  if not user_option in options:
    print("opción no válida")
    continue
    
  computer_option = random.choice(options)
  computer_option = computer_option.lower()
  
  print("user option-> ", user_option)
  print("computer option-> ", computer_option)
  
  if user_option==computer_option:
    print("Empate")
  elif user_option == "piedra":
    if computer_option=="tijera":
      print("piedra gana a tijera")
      print("user ganó")
      users_wins += 1
    else: 
      print("papel gana a piedra")
      print("computer gana")
      computer_wins += 1       
  elif user_option == "papel":
    if computer_option=="piedra":
      print("papel gana a piedra")
      print("user ganó")
      users_wins += 1
    else: 
      print("piedra gana a tijera")
      print("computer gana")
      computer_wins += 1
  elif user_option == "tijera":
    if computer_option=="papel":
      print("tijera gana a papel")
      print("user ganó")
      users_wins += 1
    else: 
      print("piedra gana a tijera")
      print("computer gana")
      computer_wins += 1
  if computer_wins == 2:
    print("el ganador es la computador")
    break
  if users_wins == 2:
    print("el ganador es el usuario")
    break 
  rounds += 1 