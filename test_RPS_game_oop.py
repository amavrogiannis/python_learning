from RPS_game_oop import *
import pytest
import random
import mock
import builtins

GAME_OBJECTS = ["rock", "paper", "scissors"]

def test_human_player():
    test_var = random.choice(GAME_OBJECTS)
    with mock.patch.object(builtins, 'input', lambda _: test_var):
        if test_var in GAME_OBJECTS:
            assert human_player() == test_var
        else: 
            exit(1)

def test_init_score():
    scoreboard = Scoreboard()
    assert scoreboard.human_score == 0
    assert scoreboard.robot_score == 0

def test_add_human_score():
    scoreboard = Scoreboard()
    scoreboard.add_human_score()
    assert scoreboard.human_score == 3

def test_add_robot_score():
    scoreboard = Scoreboard()
    scoreboard.add_robot_score()
    assert scoreboard.robot_score == 3

def test_draw():
    scoreboard = Scoreboard()
    scoreboard.draw()
    assert scoreboard.human_score == 1
    assert scoreboard.robot_score == 1

def test_game_decision():
    