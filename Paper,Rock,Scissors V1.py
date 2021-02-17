player1 = 'rock'
player2 = 'scissors'

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




