import random


def generate_choice():
  """
  Args:
    None
    
  Returns:
    string: rock, paper, or scissors based on random number generator.
  """
  choice = random.randint(0,2)
  if choice == 0:
    return "rock"
  elif choice == 1:
    return "paper"
  else:
    return "scissors"
    
    
def get_user_choice():
  """
  Args:
    None
    
  Returns:
    string: rock, paper, or scissors based on user input.
  """
  while(True):
    choice = input("Rock, paper, or scissors? ")
    # if correct user input, break from loop and return choice
    if choice.lower() == "rock" or choice.lower() == "paper" or choice.lower() == "scissors":
      break
    else:
      print("Invalid input.  Please choose rock, paper, or scissors. ")
    
  return choice.lower()
  

def print_battle(computer_choice, user_choice):
  """
  Args:
    computer_choice (string): computer's choice
    user_choice (string): user's choice
    
  Returns:
    None
  """
  # print choices
  print("Computer chose: ", computer_choice)
  print("User chose: ", user_choice)
  
  # determine win/loss/tie
  if computer_choice == "rock" and user_choice == "scissors":
    print("Computer wins!")
  elif computer_choice == "rock" and user_choice == "paper":
    print("User wins!")
  elif computer_choice == "paper" and user_choice == "rock":
    print("Computer wins!")
  elif computer_choice == "paper" and user_choice == "scissors":
    print("User wins!")
  elif computer_choice == "scissors" and user_choice == "paper":
    print("Computer wins!")
  elif computer_choice == "scissors" and user_choice == "rock":
    print("User wins!")
  elif computer_choice == user_choice:
    print("Tie!  Play again.")