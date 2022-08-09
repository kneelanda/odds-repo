import pandas as pd
import requests
import json
from datetime import datetime
from dotenv import load_dotenv
from app import APP_ENV
import os

API_KEY = os.getenv("API_KEY")

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
        with open('output.txt', 'w') as f:
            print("Moneyline for the Next "+str(len(bookmakers_lst))+" Games:", file=f)
            print("     ", file=f)
            print("Game 1: Home",response_df_five["home_team"][0],"versus Away",response_df_five["away_team"][0],"-- Event Date:",response_df_five["event_date"][0], file=f)
            print("Game 2: Home",response_df_five["home_team"][1],"versus Away",response_df_five["away_team"][1],"-- Event Date:",response_df_five["event_date"][1], file=f)
            print("Game 3: Home",response_df_five["home_team"][2],"versus Away",response_df_five["away_team"][2],"-- Event Date:",response_df_five["event_date"][2], file=f)
            print("Game 4: Home",response_df_five["home_team"][3],"versus Away",response_df_five["away_team"][3],"-- Event Date:",response_df_five["event_date"][3], file=f)
            print("Game 5: Home",response_df_five["home_team"][4],"versus Away",response_df_five["away_team"][4],"-- Event Date:",response_df_five["event_date"][4], file=f)
            for game in bookmakers_lst:
                print("     ", file=f)
                print("     ", file=f)
                print("Game:",game[0]["markets"][0]["outcomes"][0]["name"],"versus",game[0]["markets"][0]["outcomes"][1]["name"], file=f)
                print("Moneylines from All Bookmakers", file=f)
                print("Number of Bookmakers:",len(game), file=f)
                print("-----------------------", file=f)
                for bookmaker in game:
                    print(bookmaker["markets"][0]["outcomes"][0]["name"],bookmaker["markets"][0]["outcomes"][0]["price"], file=f)
                    print(bookmaker["markets"][0]["outcomes"][1]["name"],bookmaker["markets"][0]["outcomes"][1]["price"], file=f)
                    print("Bookmaker:",bookmaker["title"], file=f)
                    print("              ", file=f)
    except:
        print("Sorry, that's not a valid sport or there are no moneylines available. Please enter a major US sport and try again.")

    with open('output.txt', 'r') as f:
        print(f.read())
        
money_lines()

