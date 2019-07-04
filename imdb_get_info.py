from bs4 import BeautifulSoup
import requests


class Movie:
    def __init__(self, tt, title, stars = None, genres = None, country=None, storyline='', year='', director='' ):
        self.tt = tt
        self.title = title
        self.year = year
        self.director = director
        self.stars = []
        self.genres = []
        self.country = []
        self.storyline = storyline

    def __str__(self):
        return "Title : {} \n" \
               "tt : {} \n" \
               "Directory : {} \n" \
               "Year : {}\n" \
               "Country : {}".format(self.title, self.tt, self.director, self.year, self.country)


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


def get_film_details_page(tt, title):
    movie = Movie(tt,title)
    """Function that create sets of Movie objects that match film title
    :param tt:tt in imdb
    :param title:title of the movie"""
    url_movie = 'https://www.imdb.com/title/tt' + str(tt) + '/?ref_=fn_tt_tt_1'
    print(url_movie)
    resp = requests.get(url_movie)
    html_soup = BeautifulSoup(resp.text, 'html.parser')
    type(html_soup)
    movie_det1 = html_soup.find('div', class_='title_wrapper')

# Extract year
    try:
        year = movie_det1.h1.a.text
    except:
        year = ''
    movie.year = year

# Extract director
    movie_dir_stars = html_soup.find('div', class_='credit_summary_item')
    for i in movie_dir_stars:
        if "<a href" in str(i):
            director = str(i).split(">")[1].strip("</a")
            movie.director = director

# Extract country
    movie_country = html_soup.find('div', id='titleDetails')
    #print(movie_country.find('div',class_='txt-block'))
    m_c2 = movie_country.find('div', class_='txt-block')
    for i in m_c2:
        queue = 0
        if "country" in str(i):
            country_f = ''
            for j in str(i).split(">")[1].split("<")[0]:
                country_f = country_f + j
            movie.country.append(country_f)

    print(movie)
