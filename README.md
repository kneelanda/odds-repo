### odds-repo
Repo for out odds project.

### Running from Local Environment
Use Anaconda to create and activate a new virtual environment, perhaps called "sports-env":

```sh
conda create -n sports-env python=3.8
conda activate sports-env
```

```sh
pip install -r requirements.txt
```

```
python -m app.odds_script  
```


### Web App

To run the web app:

```sh
FLASK_APP=web_app flask run
```

The 'Home' button will return you to the home page. The 'Run App' button will let you run the script. 
Choose the sport which you would like to see results for and hit "Show Me Da Money" to see the active events and money lines. 