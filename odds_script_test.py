# testing using pytest

from odds_script import money_lines

def test_money_lines():
    message = "Sorry, that's not a valid sport or there are no moneylines available. Please enter a major US sport and try again."
    assert money_lines(sport="americanfootball_nfl") == None
    assert money_lines(sport=None) != message
    