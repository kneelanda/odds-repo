import pandas as pd
import plotly.express as px
import requests
import json

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
        response_df = pd.DataFrame(response_lst)
#found above syntax at https://favtutor.com/blogs/list-to-dataframe-python
        bookmakers_lst = response_df["bookmakers"].head(5).tolist()
        print("Moneyline for the Next "+str(len(bookmakers_lst))+" Games:")
        print("     ")
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
        print("Sorry, that's not a valid sport. Please enter a major US sport and try again.")

#americanfootball_nfl
sport = input("Please enter your sport:")
money_lines(sport)