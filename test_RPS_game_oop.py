from RPS_game_oop import human_player, Scoreboard, main, game_decision, GAME_OBJECTS
import builtins, pytest, random, mock, unittest, sys, io


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

winning_obj = GAME_OBJECTS[0]
lossing_obj = GAME_OBJECTS[2]
draw_obj = GAME_OBJECTS[1]

@pytest.fixture
def test_win():
    scoreboard == Scoreboard()
    result = game_decision(scoreboard, winning_obj, lossing_obj)
    assert result == 'You WIN! rock smashes scissors'
    assert scoreboard == 3

@pytest.Class.from_parent.__class__()
def test_lose():
    scoreboard == Scoreboard()
    result = game_decision(scoreboard, winning_obj, lossing_obj)
    assert result == 'You LOSE! rock smashes scissors'
    assert scoreboard == 3

@pytest.fixture
def test_draw():
    scoreboard == Scoreboard()
    result = game_decision(scoreboard, draw_obj, draw_obj)
    assert result == 'This round is a DRAW'
    assert scoreboard.draw == 1
