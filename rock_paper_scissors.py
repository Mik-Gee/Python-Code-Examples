import random

def rock_paper_scissors():
    player = input("What is your choice: 'r' for rock, 's' for scissor, 'p' for paper: ")
    choices = ['r','s','p']
    opponent = random.choices(choices)
    
    if player == opponent:
        return print(f"It's a tie! Choice is {opponent}")
    if check_win(player,opponent):
        return print(f"Congrats! You Won! Choice is {opponent}")
    if  check_win(player,opponent) != True:
        return print(f"You Lost! Choice is {opponent}")
            
def check_win(user,computer):
    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        return True
    else:
        return False
        
rock_paper_scissors()
    