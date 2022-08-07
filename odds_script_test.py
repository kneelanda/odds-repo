# testing using pytest

from odds_script import money_lines

def test_money_lines():
    
    assert money_lines(sport="americanfootball_nfl") == None
    
    