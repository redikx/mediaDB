from bs4 import BeautifulSoup
import requests


def get_possible_films_list(film_title: str) -> []:
    """
    Function that generates list of all possible films matches input strin
    :param film_title: string searching, white spaces are then converted to +
    :return: list [ tt, title ]
    """
    film_search = film_title.replace(' ', '+')
    url_movie = 'https://www.imdb.com/find?ref_=nv_sr_fn&q=' + film_search + '&s=tt&ref_=fn_al_tt_mr'
    resp = requests.get(url_movie)
    html_soup = BeautifulSoup(resp.text, 'html.parser')
    type(html_soup)

    movie_found = html_soup.find_all('td', class_='result_text')
    movie_list = []
    for i in movie_found:
        if '<td class="result_text"> <a href="/title' in str(i) and 'Episode' not in str(i) \
                and '(Short)' not in str(i) and '(Video)' not in str(i) \
                and '(TV Series)' not in str(i) and '(in development)' not in str(i)\
                and '(Video Game)' not in str(i) and '(TV Movie)' not in str(i)\
                and 'Documentary' not in str(i) and film_title in str(i):
            movie_list.append([str(i).split(">")[1].strip('<a href="/title/'), str(i).split(">")[2].strip("</a")])
    return movie_list

def get_film_details(tt):
    url_movie = 'https://www.imdb.com/title/tt' + str(tt) + '/?ref_=fn_tt_tt_1'
    print(url_movie)