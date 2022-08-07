import pandas as pd
import plotly.express as px
import requests
import json
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
        response_df = pd.DataFrame(response_lst)
        response_df_five = response_df.head(5)
#found above syntax at https://favtutor.com/blogs/list-to-dataframe-python
        bookmakers_lst = response_df_five["bookmakers"].tolist()
        with open('output.txt', 'w') as f:
            print("Moneyline for the Next "+str(len(bookmakers_lst))+" Games:", file=f)
            print("     ", file=f)
            print("Game 1: Home",response_df_five["home_team"][0],"versus Away",response_df_five["away_team"][0],"-- Start Time in UTC:",response_df_five["commence_time"][0], file=f)
            print("Game 2: Home",response_df_five["home_team"][1],"versus Away",response_df_five["away_team"][1],"-- Start Time in UTC:",response_df_five["commence_time"][1], file=f)
            print("Game 3: Home",response_df_five["home_team"][2],"versus Away",response_df_five["away_team"][2],"-- Start Time in UTC:",response_df_five["commence_time"][2], file=f)
            print("Game 4: Home",response_df_five["home_team"][3],"versus Away",response_df_five["away_team"][3],"-- Start Time in UTC:",response_df_five["commence_time"][3], file=f)
            print("Game 5: Home",response_df_five["home_team"][4],"versus Away",response_df_five["away_team"][4],"-- Start Time in UTC:",response_df_five["commence_time"][4], file=f)
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
        print("Sorry, that's not a valid sport. Please enter a major US sport and try again.")

money_lines()