import json
import requests_with_caching

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movies_from_tastedive("Bridesmaids")
# get_movies_from_tastedive("Black Panther")

def get_movies_from_tastedive(movie):
    args = {'q': movie, 'type':'movies', 'limit':5}
    baseUrl = 'https://tastedive.com/api/similar'
    response = requests_with_caching.get(baseUrl, params = args)
    d = json.loads(response.text)
    return d

#-------------------------------

def extract_movie_titles(d):
    response = list()
    movies = d['Similar']['Results']
    for m in movies:
        response.append(m['Name'])
    return response

#---------------------------------------

def get_related_titles(lst):
    rm = list()
    for movie in lst:
        r = get_movies_from_tastedive(movie)
        ls = extract_movie_titles(r)
        rm = rm + filter(lambda movie: movie not in rm, ls)
    return rm

#----------------------------------

def get_movie_data(movie):
    args = {'t': movie, 'r':'json'}
    baseUrl = 'http://www.omdbapi.com/'
    response = requests_with_caching.get(baseUrl, params = args)
    d = json.loads(response.text)
    return d

#--------------------------------

def get_movie_rating(d):
    rate = 0
    if len(d['Ratings']) > 1:
        if d['Ratings'][1]['Source'] == 'Rotten Tomatoes':
            rate = int(d['Ratings'][1]['Value'][:2])
    return rate

#----------------------------------

def get_sorted_recommendations(lst):
    rank = dict()
    for movie in get_related_titles(lst):
        rank[movie] = get_movie_rating(get_movie_data(movie))

    response = [i[0] for i in sorted(rank.items(), key=lambda item: (item[1], item[0]), reverse=True)]
    return response

#-----------------------------
