import json
film={
    "title": "AAle ja nie będę tego robił!",
    "release_year": 1969,
    "won_oscar":True,
    "actors":("Arkadiusz Włodarczyk","Wioletta Włodarczyk"),
    "budget": None,
    "credits":{
        "director": "Arkadiusz Włodarczyk",
        "writer": "Alan Burger",
        "animator": "Anime Animatrix"
    }
}
encodedFilm=json.dumps(film,ensure_ascii=False)
#print(encodedFilm)
with open("sample2.json","w",encoding="UTF-8") as file:
    json.dump(film,file,ensure_ascii=False, indent=6,sort_keys=True)