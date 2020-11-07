# lookism scraper  
lookism scraper, scrapes user posts from multiple useres. Stores list in json. \
look at json file for example


## install libraries and dependencies before running

run "pip install -r requirements.txt"

if you want env: \
"pip install pipenv" \
"pipenv install -r requirements.txt"

## Running 
typing "python run.py" should start the scraping. You can modify the url_list variable for different users \
also check url_list for url formats for the scraper 

or if you want to use pipenv: \
"pipenv run python run.py"

## Docker 
there is a dockerfile, run the build_run.sh (this is for linux only) you probably need to run "chmod +x build_run.sh" to make it executable.

if not using linux. Look in the build_run.sh and type in the docker comamnds 

it should spit out a log and json file in your current directory if everything goes right 