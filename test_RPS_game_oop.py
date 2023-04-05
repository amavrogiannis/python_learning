from RPS_game_oop import *
import random
import sys

# Variables
EXPECTED_OBJECTS = ["rock", "paper", "scissors"]

def test_robot_player():
    result = robot_player()
    assert result in EXPECTED_OBJECTS

def game_decision():
    