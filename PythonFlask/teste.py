import urllib.request, json

url = "https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=462fbe53e2f67835e73f92d9a3c6c4a3"

resposta = urllib.request.urlopen(url)

print(resposta)