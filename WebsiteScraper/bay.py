#Scrape the all link by href in website page
#To Download with youtube-dl :
#	youtube-dl --external-downloader aria2c -o "%(autonumber)s.%(title)s.%(ext)s" -a file.txt


from bs4 import BeautifulSoup, SoupStrainer
import requests
import lxml
import re

url = "linkofpage" #paste the link of page you want to scrape

page = requests.get(url)    
data = page.text
soup = BeautifulSoup(data,"lxml")

for link in soup.find_all('a'):
    matched = re.search("view",f"{link}")
    if matched:
        matched_link = link.get('href')
        with open("file.txt",'a+') as f:
            f.write(f"baselinkofpage{matched_link} \n") #paste base link of website Ex:www.google.com






