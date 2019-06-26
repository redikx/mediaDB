from imdb_get_info import get_possible_films_list

fl = get_possible_films_list('Omen')
print("RESULTS : ")
for i in fl:
    print(i)
print('*'*100)