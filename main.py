import random
def game():
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
          print("Nice! You guessed the number right! It took you " + str(gameover) + " tries.")
          win = True
          start = False
          break
    break

  if win == True:
    print("Congrats! You won in " + str(gameover) + " tries." )
  else:
    print("You lose! The number was " + str(compnum) + " . :(")


  option = input("Would you like to play again? Y/N ")
  if option == "Y" or option == "y":
    game()

  else:
    print("ok. goodbye!")
game()

  