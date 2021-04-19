from getpass import getpass
from time import sleep
from random import randint
import os
os.system('cls')
print("\n\n\n\n")
print('...................Rock Paper Scissor.............'.center(100))
print("\n\n\n")
p1=getpass('player1 choice: '.rjust(50)).lower().strip()
print('\n\n')
p2=getpass('player2 choice: '.rjust(50)).lower().strip()
print('\n\n')
p1_won=[
(p1=='rock' and p2=='scissor'),
(p1=='scissor' and p2=='paper'),
(p1=='paper' and p2=='rock')
]
print('\n\n')
print("Processing".rjust(50),end='')
for i in range(randint(3,8)):
      print(".",end='',flush=True)
      sleep(1)
print('\n\n')
print(f'Choice of player 1 is : {p1:<10}'.center(100))
print(f'Choice of player 2 is : {p2:<10}'.center(100))
print('\n\n')
if any(p1_won):
      print("Player1 won the Game".center(100))
elif p1==p2:
      print('Match Tie'.center(100))
else:
     print('Player2 won the Game'.center(100))
print('\n\n\n')
input('.......................press any key to exit.................'.center(100))
os.system('cls')

       