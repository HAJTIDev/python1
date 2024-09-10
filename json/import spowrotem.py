import json,pprint
encodedFilm='{"title": "AAle ja nie będę tego robił!", "release_year": 1969, "won_oscar": true, "actors": ["Arkadiusz Włodarczyk", "Wioletta Włodarczyk"], "budget": null, "credits": {"director": "Arkadiusz Włodarczyk", "writer": "Alan Burger", "animator": "Anime Animatrix"}}'
decodedMovie=json.loads(encodedFilm)
#print(decodedMovie)
with open("sample2.json",encoding="UTF-8") as file:
    wynik=json.load(file)
print(wynik)
pprint.pprint(wynik)