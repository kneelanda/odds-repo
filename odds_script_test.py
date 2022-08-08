# testing using pytest

from odds_script import money_lines

def test_money_lines():
    error_message = "Error"
    
    assert money_lines(sport="americanfootball_nfl") == None
    assert money_lines(sport=None) != error_message

    
   
