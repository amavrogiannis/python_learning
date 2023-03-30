# pylint: disable=C0103
"""This is a Rock Paper Scissors game"""
import random
import sys

# """ Defining objects """
GAME_OBJECTS = ["rock", "paper", "scissors"]
CHOICE = ["y", "n"]

class Scoreboard:
    def __init__(self, human_score = 0, robot_score = 0):
        self.human_score = human_score
        self.robot_score = robot_score

    def add_human_score(self):
        self.human_score += 3

    def add_robot_score(self):
        self.robot_score += 3

    def draw(self):
        self.human_score += 1
        self.robot_score += 1

    def game_scores(self):
        print("GAME SUMMARY:")
        return f"Human: {self.human_score}\nComputer: {self.robot_score}"

""" Human selected object """
def human_player():
    """ The user_input will require the person to imput on of the selection in GAME_OBJECTS """
    while True:
        user_input = input("Please input your object 👉 ").lower()
        if user_input in GAME_OBJECTS:
            print(f"👤 You selected 👉 {user_input.upper()}")
            return user_input
        # pylint: disable=C0303
        print(f"This object is invalid, please select one of the following:\n {GAME_OBJECTS}") 

# """ Robot's selected object against the human """
def robot_player():
    """ Random library set to select random object in GAME_OBJECTS"""
    robot_selection = random.choice(GAME_OBJECTS)
    print(f"🤖 Robot selected 👉 {robot_selection.upper()}")
    return robot_selection

# """ This function writen the game decision """
def game_decision(scoreboard, user_input, robot_selection):
    """ This generator is set to decide who wins according to human vs computer selected object """
    if user_input == robot_selection:
        print("This round is a DRAW")
        # score value on resulting draw
        scoreboard.draw()
    elif user_input == GAME_OBJECTS[0]:
        if robot_selection == GAME_OBJECTS[1]:
            print(f"You LOSE! {robot_selection} covers {user_input}")
            # score value on win result
            scoreboard.add_robot_score()
        else:
            print(f"You WIN! {user_input} smashes {robot_selection}")
            # score value on win result
            scoreboard.add_human_score()
    elif user_input == GAME_OBJECTS[1]:
        if robot_selection == GAME_OBJECTS[2]:
            print(f"You LOSE! {robot_selection} cuts {user_input}")
            # score value on win result
            scoreboard.add_robot_score()
        else:
            print(f"You WIN! {user_input} covers {robot_selection}")
            # score value on win result
            scoreboard.add_human_score()
    elif user_input == GAME_OBJECTS[2]:
        if robot_selection == GAME_OBJECTS[0]:
            print(f"You LOSE! {robot_selection} smashes {user_input}")
            # score value on win result
            scoreboard.add_robot_score()
        else:
            print(f"You WIN! {user_input} cuts {robot_selection}")
            # score value on win result
            scoreboard.add_human_score()

# """ This function allows the user to resume the game """
def player_resume():
    """ Ask the user to resume the game with "y" or "n" options """
    while True:
        resume_game = input("Do you want to resume play? y/n: ").lower()
        if resume_game in CHOICE:
            if resume_game == "y":
                break
            if resume_game == "n":
                sys.exit()
        print(f"This selection is invalid, need to be {CHOICE}")

def main():
    """ This is the main function which pull other functions """
    while True:
        scoreboard = Scoreboard()
        while True:
            user_input = human_player()
            robot_selection = robot_player()
            game_decision(scoreboard, user_input, robot_selection)
            print(scoreboard.game_scores())
            player_resume()

# pylint: disable=C0304
if __name__ == '__main__':
    main()