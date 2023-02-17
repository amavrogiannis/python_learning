"""This is a Rock Paper Scissors game"""
import random

""" Defining objects """
object_list = ["rock", "paper", "scissors"]

""" Human selected object """
def human_player():

    while True:
        user_input = input("Please input your object 👉 ").lower()
        if user_input in object_list:
            return print(f"👤 You selected 👉 {user_input.upper()}")
        print(f"This object is invalid, please select one of the following: \n {object_list}") 
    return user_input

""" Robot's selected object """
def robot_player():
    robot_selection = random.choice(object_list)
    print(f"🤖 Robot selected 👉 {robot_selection.upper()}")
    return robot_selection

""" Decision """
def game_decision(user_input, robot_selection):

    if human_player(user_input) == robot_player(robot_selection):
        print("This round is a DRAW")
    elif human_player(user_input) == object_list[0]:
        if robot_player(robot_selection) == object_list[1]:
            print(f"You lose! {robot_player(robot_selection)} covers {human_player(user_input)}")
        else:
            print(f"You win! {human_player(user_input)} smashes {robot_player(robot_selection)}")
    
    elif human_player(user_input) == object_list[1]:
        if robot_player(robot_selection) == object_list[2]:
            print(f"You lose! {robot_player(robot_selection)} cuts {human_player(user_input)}")
        else:
            print(f"You win! {human_player(user_input)} covers {robot_player(robot_selection)}")

    elif human_player(user_input) == object_list[2]:
        if robot_player(robot_selection) == object_list[0]:
            print(f"You lose! {robot_player(robot_selection)} smashes {human_player(user_input)}")
        else:
            print(f"You win! {human_player(user_input)} cuts {robot_player(robot_selection)}")


def main():
    human_player()
    robot_player()
    game_decision(user_input, robot_selection)


main()