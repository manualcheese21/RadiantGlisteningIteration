import random

compnum = random.randint(0,10)
start = True
gameover = 5
win = False
while start == True:
  while gameover > 0:
    guessnumber = int(input("Guess the number between 0 and 10! "))
    if(guessnumber < 0 or guessnumber > 10):
      print("Invalid Number. Enter a number between 1 and 10")
    else:
      if guessnumber > compnum:
        print("Too big number")
        gameover -=1
        print("You have " + str(gameover) + " attempts left.")
      elif guessnumber < compnum:
        print("Too small number")
        gameover -=1
        print("You have " + str(gameover) + " attempts left.")
      elif guessnumber == compnum:
        print("Nice! You guessed the number right!")
        win = True
        start = False

if win == True:
  print("Congrats! You won in "  str(gameover) + " tries." )
      


              