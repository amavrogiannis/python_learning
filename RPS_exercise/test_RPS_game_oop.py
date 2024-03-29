from RPS_game_oop import human_player, Scoreboard, main, game_decision, player_resume, GAME_OBJECTS
import builtins, pytest, random, mock, unittest, sys, io

scoreboard = Scoreboard()

'''Testing Scoreboard class - which objects are adding 3 points to the winner (Human vs Robot) and adding 1 point each, when the round is tied.'''
class TestScoreboard(unittest.TestCase): 
    def test_add_human_score(self):
        print("\nRunning test_add_human_score ...")
        hum_score = Scoreboard(0, 0)
        hum_score.add_human_score()
        self.assertEqual(hum_score.game_scores(), f"Human: {0 + 3}\nComputer: {0 + 0}")
    def test_add_robot_score(self):
        print("\nRunning test_add_robot_score ...")
        rob_score = Scoreboard(0, 0)
        rob_score.add_robot_score()
        self.assertEqual(rob_score.game_scores(), f"Human: {0 + 0}\nComputer: {0 + 3}")
    def test_draw(self):
        print("\nRunning test_draw ...")
        draw_score = Scoreboard(0, 0)
        draw_score.draw()
        self.assertEqual(draw_score.game_scores(), f"Human: {0 + 1}\nComputer: {0 + 1}")

def test_human_player():
    test_var = random.choice(GAME_OBJECTS)
    with mock.patch.object(builtins, 'input', lambda _: test_var):
        if test_var in GAME_OBJECTS:
            assert human_player() == test_var
        else: 
            return 1

win = "scissors"
lose = "paper"
def test_win(capsys):
    scoreboard = Scoreboard(0,0)
    game_decision(scoreboard, user_input=win, robot_selection=lose)

    capture = capsys.readouterr()
    capture_stdout = capture.out.strip()

    assert 'You WIN!' in capture_stdout

    assert scoreboard.human_score == 3
    assert scoreboard.robot_score == 0 

def test_lose(capsys):
    scoreboard = Scoreboard(0,0)
    game_decision(scoreboard, user_input=lose, robot_selection=win)

    capture = capsys.readouterr()
    capture_stdout = capture.out.strip()

    assert 'You LOSE!' in capture_stdout

    assert scoreboard.human_score == 0
    assert scoreboard.robot_score == 3

def test_draw(capsys):
    scoreboard = Scoreboard(0,0)
    result = game_decision(scoreboard, user_input=win, robot_selection=win)

    capture = capsys.readouterr()
    capture_stdout = capture.out.strip()

    assert 'DRAW' in capture_stdout

    assert scoreboard.human_score == 1
    assert scoreboard.robot_score == 1
