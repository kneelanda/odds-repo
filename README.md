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

Add a new file called "odd_script_test.py" and insert the below code to run your test:
```
from odds_script import money_lines

def test_money_lines():
    assert money_lines(sport="americanfootball_nfl") == None
```

When tests are done, make sure to push your code to Github under a new branch (include "testing" in the branch name) and create a Pull Request to see updated checks.