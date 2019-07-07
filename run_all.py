from imdb_get_info import get_possible_films_list
from imdb_get_info import get_film_details_page

title_search = "Assassin"
fl = get_possible_films_list(title_search)
found_exact = 0
for i in fl:
    #print(i)
    imovie = get_film_details_page(i[0],i[1])
    if imovie.title == title_search:
        print(imovie)
        found_exact+=1
        break

if found_exact == 0:
    num_on_list = 0
    print("No match, want to select from list?")
    for j in fl:
        print(str(num_on_list) + ": " + str(j))
        num_on_list+=1
    #TODO : prompt to enter list number, then return movie
print('*'*100)




