import pandas as pd
import plotly.express as px
import requests
import json
from datetime import datetime

API_KEY = "29c6f90345f591ee9428c75b7bb1f4ff"

def money_lines(sport=None):
    if sport==None:
        sport="americanfootball_nfl"
    try:
        url = "https://api.the-odds-api.com/v4/sports/"+sport+"/odds/?apiKey="+API_KEY+"&regions=us&markets=h2h&oddsFormat=american"
#url syntax provided by https://the-odds-api.com/
        response = requests.get(url)
#code adapted from web requests excercise in class
        response_lst = json.loads(response.text)
        response_df_five  = pd.DataFrame(response_lst).head(5)
        date_time_list = [datetime.strptime(time,'%Y-%m-%dT%H:%M:%SZ').date() for time in response_df_five["commence_time"]]
        response_df_five["event_date"] = date_time_list
#found above syntax at https://favtutor.com/blogs/list-to-dataframe-python
        bookmakers_lst = response_df_five["bookmakers"].tolist()
        print("Moneyline for the Next "+str(len(bookmakers_lst))+" Games:")
        print("     ")
        print("Game 1: Home",response_df_five["home_team"][0],"versus Away",response_df_five["away_team"][0],"--",response_df_five["event_date"][0])
        print("Game 2: Home",response_df_five["home_team"][1],"versus Away",response_df_five["away_team"][1],"--",response_df_five["event_date"][1])
        print("Game 3: Home",response_df_five["home_team"][2],"versus Away",response_df_five["away_team"][2],"--",response_df_five["event_date"][2])
        print("Game 4: Home",response_df_five["home_team"][3],"versus Away",response_df_five["away_team"][3],"--",response_df_five["event_date"][3])
        print("Game 5: Home",response_df_five["home_team"][4],"versus Away",response_df_five["away_team"][4],"--",response_df_five["event_date"][4])
        for game in bookmakers_lst:
            print("     ")
            print("     ")
            print("Game:",game[0]["markets"][0]["outcomes"][0]["name"],"versus",game[0]["markets"][0]["outcomes"][1]["name"])
            print("Moneylines from All Bookmakers")
            print("Number of Bookmakers:",len(game))
            print("-----------------------")
            for bookmaker in game:
                print(bookmaker["markets"][0]["outcomes"][0]["name"],bookmaker["markets"][0]["outcomes"][0]["price"])
                print(bookmaker["markets"][0]["outcomes"][1]["name"],bookmaker["markets"][0]["outcomes"][1]["price"])
                print("Bookmaker:",bookmaker["title"])
                print("              ")
    except:
        print("Sorry, that's not a valid sport or there are no moneylines available. Please enter another major US sport and try again.")

#americanfootball_nfl
#basketball_nba
#baseball_mlb
sport = input("Please enter your sport:")
money_lines(sport)