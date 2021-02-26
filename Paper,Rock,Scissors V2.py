#needed to turn our rps v1 into a function
#first need to create a function def rps()
#because we are adding additional data to our function our parameters will be (player1,player2)
def rps(player1,player2):

#because we have turned our variables into a function we need to correctly indent the block of code below to put it in the function or else it will not be considered part of the function and will not run and will proudce an error
  if player1 == player2:
    print("It's a tie")
  elif player1 == 'rock' and player2 == 'paper':
    print('Player 2 wins')
  elif player1 == 'rock' and player2 == 'scissors':
    print('Player 1 wins')
  elif player1 == 'paper' and player2 == 'rock':
    print('Player 1 wins')
  elif player1 == 'paper' and player2 == 'scissors':
    print('Player 2 wins')
  elif player1 == 'scissors' and player2 == 'rock':
    print('Player 2 wins')
  else:
    print('Player 1 wins')
#here is where we put the arguments rock, scissors. 
#rock is the value for variable player1 and scissors is the value for variable player2 
#by doing this we are involking (calling) the arguments for the parameter in line 4
rps("rock", "scissors")




