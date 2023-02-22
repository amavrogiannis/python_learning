# """This is a Rock Paper Scissors game"""
import random

# """ Defining objects """
object_list = ["rock", "paper", "scissors"]

# """ Human selected object """
def human_player():
    while True:
        user_input = input("Please input your object 👉 ").lower()
        if user_input in object_list:
            print(f"👤 You selected 👉 {user_input.upper()}")
            return user_input
        print(f"This object is invalid, please select one of the following:\n {object_list}") 

# """ Robot's selected object """
def robot_player():
    robot_selection = random.choice(object_list)
    print(f"🤖 Robot selected 👉 {robot_selection.upper()}")
    return robot_selection

# """ Decision """
def game_decision(user_input, robot_selection):
    if user_input == robot_selection:
        print("This round is a DRAW")
    elif user_input == object_list[0]:
        if robot_selection == object_list[1]:
            print(f"You LOSE! {robot_selection} covers {user_input}")
        else:
            print(f"You WIN! {user_input} smashes {robot_selection}")
    elif user_input == object_list[1]:
        if robot_selection == object_list[2]:
            print(f"You LOSE! {robot_selection} cuts {user_input}")
        else:
            print(f"You WIN! {user_input} covers {robot_selection}")
    elif user_input == object_list[2]:
        if robot_selection == object_list[0]:
            print(f"You LOSE! {robot_selection} smashes {user_input}")
        else:
            print(f"You WIN! {user_input} cuts {robot_selection}")

def main():
    # """ This is the main function """
    user_input = human_player()
    robot_selection = robot_player()
    game_decision(user_input, robot_selection)

# """ Execure main function """
main()