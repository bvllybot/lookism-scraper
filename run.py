#%%
import requests
import bs4 as bs
import re
import json 

url_list = [
    "https://lookism.net/search/142107/",
    "https://lookism.net/search/141768"
]


base_url = "https://lookism.net" 
def make_new_url(base, hrefs):
    """
    construct new url afterwards takes base_url and hrefs as argument
    """
    for href in hrefs:
        if re.search('^/search/\d+/$', href['href']): # any #'s between /search/ and / 
            new_url = f'{base}{href["href"]}'
            return new_url
            
def get_older_posts(hrefs):
    """
    find href in hrefs with older?before in string
    """
    print('in get_older_posts')
    for href in hrefs:
        #print(href['href'])
        if 'older?before' in href['href']:
            print('found older posts')
            print(href['href'])
            return lookism_scrape(f'{base_url}{href["href"]}')

def loop_through_pages(url):
    pass 

def make_request(url):
    res = requests.get(f"{url}")
    return res 

shitposts_list = []
def get_shitposts(shitposts):
    """
    get shit posts from user and put them in a list
    """
    for shitpost in shitposts:
        filter = re.compile(r'[\n\t\r]')
        sub = filter.sub(" ", shitpost.text)
        shitposts_list.append(sub)

def lookism_scrape(url):
    """
    scrape lookism using requests and bs4 
    """
    for i in range(1,6):
        if i == 1: 
            res = requests.get(url)
            print(url)
        if i > 1: 
            url =  f"{url}?page={i}"
            res = requests.get(url)
            print(url)
        content = res.content
        soup = bs.BeautifulSoup(content, 'lxml')
        shitposts = soup.findAll('div', {'class': 'contentRow-snippet'})
        hrefs = soup.findAll('a', href=True, text=True)
        url = make_new_url(base_url, hrefs)

        get_shitposts(shitposts)

        #for shitpost in shitposts:
            #print(shitpost.text)

        #print('**********************************************************') 
        #print(i)
        if i == 5:
            ##  call older posts functions
            try:
                get_older_posts(hrefs) 
            except:
                print('error looks like no more older posts')
                return 
for item in url_list:
    lookism_scrape(item)
with open('shitposts.json', 'w') as f:
    json.dump(shitposts_list, f)
#print(shitposts_list)
#%% this area is for testing
#import requests
#import bs4 as bs
#import re

#res = requests.get(f"https://lookism.net/search/141768/older?before=1578602074")
#content = res.content
#soup = bs.BeautifulSoup(content, 'lxml')
#search2 = soup.findAll('a', {'class': 'button--link button'})
#search3 = soup.findAll('a', href=True, text=True)

#for ele in search3:
    #if re.search('^/search/\d+/$', ele['href']): # any #'s between /search/ and / 
        #print(ele['href'])