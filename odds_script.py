import pandas as pd
from pandas import read_csv
import plotly.express as px
import requests
import json



url = "https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds/?apiKey=29c6f90345f591ee9428c75b7bb1f4ff&regions=us&markets=h2h,spreads&oddsFormat=american"

response = requests.get(url)
#code adapted from web requests excercise in class

response_lst = json.loads(response.text)

response_df = pd.DataFrame(response_lst)

print(type(response_df))