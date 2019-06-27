from imdb_get_info import get_possible_films_list
from imdb_get_info import get_film_details

fl = get_possible_films_list('Omen')
for i in fl:
    print(i[1] + ":")
    get_film_details(i[0])

print('*'*100)

