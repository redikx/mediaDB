from bs4 import BeautifulSoup
import requests

def get_possible_films_list(film_title):
    film_lists = []
    film_search = film_title.replace(' ','+')
    url_movie = 'https://www.imdb.com/find?ref_=nv_sr_fn&q=' + film_search+ '&s=tt&ref_=fn_al_tt_mr'
    resp = requests.get(url_movie)
    #print(resp.text)
    html_soup = BeautifulSoup(resp.text,'html.parser')
    type(html_soup)

   #movie_found = html_soup.find_all('div', class_='findSection')
    movie_found = html_soup.find_all('td', class_='result_text')
    movie_list=[]
    for i in movie_found:
        if '<td class="result_text"> <a href="/title' in str(i) and 'Episode' not in str(i) \
                and '(Short)' not in str(i) and '(Video)' not in str(i) \
                and '(TV Series)' not in str(i) and '(in development)' not in str(i)\
                and '(Video Game)' not in str(i) and '(TV Movie)' not in str(i)\
                and film_title in str(i):
            print("Processing : " + str(i))
            print(str(i).split(">")[1].strip('<a href="/title/'))
            print(str(i).split(">")[2].strip("</a"))
            movie_list.append([str(i).split(">")[1].strip('<a href="/title/'),str(i).split(">")[2].strip("</a")])
            print("*" * 40)
    return movie_list

fl = get_possible_films_list('Omen')
print("RESULTS : ")
for i in fl:
    print(i)
print('*'*100)
