from imdb_get_info import get_possible_films_list
from imdb_get_info import get_film_details_page


fl = get_possible_films_list('It')
for i in fl:
    #print(i)
    get_film_details_page(i[0],i[1])
print('*'*100)



