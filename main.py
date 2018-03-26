import functions as fcn

# generate computer choice
computer_choice = fcn.generate_choice()

# get user input (rock, paper, scissors)
user_choice = fcn.get_user_choice()

# determine win/loss
fcn.print_battle(computer_choice, user_choice)