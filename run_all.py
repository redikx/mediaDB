from imdb_get_info import get_possible_films_list
from imdb_get_info import get_film_details_page

title_search = input("Enter movie title to search : ")
#title_search = "Assassin"
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
    print("No match, select from list?")
    for j in fl:
        movie_temp = get_film_details_page(j[0], j[1])
        row = str(num_on_list) + " Title : " + str(j[1]) + " ; Director : " + str(movie_temp.director) + " ; Year : " + str(movie_temp.year)
        print(row)
        num_on_list+=1
    #TODO : prompt to enter list number, then return movie
    chosen = input(">>")

    chosen_film = fl[int(chosen)]
    chosen_film_det = get_film_details_page(fl[int(chosen)][0], fl[int(chosen)][1])
    print(chosen_film_det)
print('*'*100)





