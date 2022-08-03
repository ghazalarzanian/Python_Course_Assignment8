import random
options=['Rock','Paper','Scissor']
Scores ={'user':0,'computer':0}
for i in range(4):
    computer_choice=random.choice(options)
    user_choice=input("play the game:(Start With Capital Letter:)))")
    print('And Computer Choice is:',computer_choice)
    if user_choice=='Rock' and computer_choice=='Paper':
        print('--------------------------------')
        print("Computer Wins")
        print('--------------------------------')
        Scores['computer']+=1
    elif computer_choice=='Rock' and user_choice=='Paper':
        print('--------------------------------')
        print("You Win")
        print('--------------------------------')
        Scores['user']+=1
    elif user_choice=='Rock' and computer_choice=='Scissor':
        print('--------------------------------')
        print('You Win')
        print('--------------------------------')
        Scores['user']+=1
    elif user_choice=='Scissor' and computer_choice=='Rock':
        print('--------------------------------')
        print('Computer Wins')
        print('--------------------------------')
        Scores['computer']+=1
    elif user_choice=='Paper' and computer_choice=='Scissor':
        print('--------------------------------')
        print('Computer Wins')
        print('--------------------------------')
        Scores['computer']+=1
    elif user_choice=='Scissor' and computer_choice=='Paper':
        print('--------------------------------')
        print('You Win')
        print('--------------------------------')
        Scores['user']+=1
    else:
        print('--------------------------------')
        print("Draw")
        print('--------------------------------')
if Scores['computer']>Scores['user']:
    print('Computer Wins')
if Scores['computer']<Scores['user']:
    print('You Win')
if Scores['computer']==Scores['user']:
    print('Draw')