### odds-repo
Repo for our odds project.

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

### Required Variables for .env file in Local Environment

API_KEY = XXXX


### Web App

To run the web app:

```sh
FLASK_APP=web_app flask run
```

The 'Home' button will return you to the home page. The 'Run App' button will let you run the script. 
Choose the sport which you would like to see results for and hit "Show Me Da Money" to see the active events and money lines. 

### Testing

In order to test using pytest make sure that pytest is installed in your virtual environment by adding "pytest" to the "requirements.txt" file.

Then install pytest by running this code again.
```
pip install -r requirements.txt
```

To run tests, insert the below in your command line:
```
pytest
```

### Deploying Web App to Heroku

To configure the web app, ensure Brew is installed:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Install Heroku CLI: 

```
brew tap heroku/brew && brew install heroku
```

Deploying to Heroku server (if already set up and configured):

```
git push heroku main
```

Changing API key (or other env variables on server):

```
heroku config:set API_KEY= XXX
```

