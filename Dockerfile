FROM python:3.8

WORKDIR /app/

COPY . /app

# linux update 
RUN apt update -y
RUN apt upgrade -y

# linux dependencies
## commented out due to problems
#RUN apt install tor -y 
#RUN apt install proxychains -y 

# python dependencies
RUN pip install -r requirements.txt 

# start tor service and start scraping using proxychains 
## problem for now  commenting out
#CMD service tor start && proxychains python run.py > logs.txt

# start scraping without proxychains 
CMD  python run.py > logs.txt
