import pandas as pd
from pandas import read_csv
import plotly.express as px
import requests
import json
from IPython.display import display
from operator import itemgetter

API_KEY = "29c6f90345f591ee9428c75b7bb1f4ff"

url = "https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds/?apiKey="+API_KEY+"&regions=us&markets=h2h&oddsFormat=american"
#url syntax provided by https://the-odds-api.com/
response = requests.get(url)
#code adapted from web requests excercise in class

response_lst = json.loads(response.text)

response_df = pd.DataFrame(response_lst)
#found above syntax at https://favtutor.com/blogs/list-to-dataframe-python

bookmakers_lst = response_df["bookmakers"].head(5).tolist()

#bookmakers_lst.sort(key=itemgetter("last_update"))
#sorted_list = sorted(bookmakers_lst, key=itemgetter("price"))

print("Moneyline for the Next "+str(len(bookmakers_lst))+" Games:")
print("     ")

for game in bookmakers_lst:
  print("     ")
  print("     ")
  print("Moneyline - All Bookmakers")
  print("Number of Bookmakers:",len(game))
  print("-----------------------")
  
  for bookmaker in game:
    print(bookmaker["markets"][0]["outcomes"][0]["name"],bookmaker["markets"][0]["outcomes"][0]["price"])
    print(bookmaker["markets"][0]["outcomes"][1]["name"],bookmaker["markets"][0]["outcomes"][1]["price"])
    print("Bookmaker:",bookmaker["title"])
    print("              ")