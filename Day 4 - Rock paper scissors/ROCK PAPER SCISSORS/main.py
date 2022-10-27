rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
response = int(input("Enter your move : 0 for ROCK, 1 for PAPER, 2 for SCISSORS\n"))
rps= [rock,paper,scissors]
if response>2 or response<0:
  print('You have choosen invalid move..SORRY:3)')
else:
  print(rps[response])
  import random
  comres=random.randint(0,2)
  print("computer chose:")
  print(rps[comres])
  if response==0:
   if comres==0:
    print('DRAW :|')
   elif comres==1:
    print('YOU LOSE :(')
   else:
    print('YOU WIN :)')
    
  elif response==1:
   if comres==0:
    print('YOU WIN :)')
   elif comres==1:
    print('DRAW :|')
   else:
    print('YOU LOSE :(')
     
  else:
   if comres==0:
    print('YOU LOSE :(')
   elif comres==1:
    print('YOU WIN :)')
   else:
    print('DRAW :|')



