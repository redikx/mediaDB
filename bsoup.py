from bs4 import BeautifulSoup
import requests

url_movie = 'https://www.imdb.com/find?ref_=nv_sr_fn&q=pet+semetary&s=all'
resp = requests.get(url_movie)
#print(resp.text)
html_soup = BeautifulSoup(resp.text,'html.parser')
type(html_soup)

#print(html_soup)

#movie_found = html_soup.find_all('div', class_='findSection')
movie_found = html_soup.find_all('td', class_='result_text')

for i in movie_found:
    movie_list=[]
    if 'href="/title' in str(i) and 'Episode' not in str(i):
        print(str(i).split(">")[1].strip('<a href="/title/'))
        print(str(i).split(">")[2].strip("</a"))
        print("*" * 40)