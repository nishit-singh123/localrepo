import random
rock='''
   --------
---'-------)
    (------)
    (-------)
      (----)
---.--(----)         
'''
paper='''
  --------
--' ------)----
        -------)
        --------)
       --------)
----.---------)          
'''
scissors=''' 
   ---------
---' -------)----
          -------)
        -----------)
        (----)
        '''
game_images=[rock,paper,scissors]
user_choice=int(input("Enter your choice: type 0 for Rock,1 for paper,2 for scissors."))
if user_choice>=3 or user_choice<0:
    print("you entered invalid number, you lose.")
else:
    print(game_images[user_choice])
    computer_choice=random.randint(0,2)
    print(computer_choice)
    print(game_images[computer_choice])
    if user_choice==computer_choice:
        print('draw')
    elif computer_choice==0 and user_choice==2:
        print('computer win')
    elif computer_choice==2 and user_choice==0:
        print('you win')
    elif computer_choice<user_choice:
        print('you win')
    elif computer_choice>user_choice:
        print('you loose')

