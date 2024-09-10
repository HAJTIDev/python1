import requests,json
def maks(name,dict):
    if place[name] != None:
        try:
            if float(place[name]) > dict[name]:
                dict[name]=float(place[name])
                dict['stacja']=place['stacja']
        except KeyError:
            dict[name]=float(place[name])
            dict['stacja']=place['stacja']
def min(name,dict):
    if place[name] != None:
        try:
            if float(place[name]) < dict[name]:
                dict[name]=float(place[name])
                dict['stacja']=place['stacja']
        except KeyError:
            dict[name]=float(place[name])
            dict['stacja']=place['stacja']
            

r=requests.get("https://danepubliczne.imgw.pl/api/data/synop/station/")
try:
    places=r.json()
    #print(tasks)
except json.decoder.JSONDecodeError:
    print("niepoprawny format")
else:
    tem={}
    pr={}
    wil={}
    sum={}
    cis={}           
    for place in places:
        maks("temperatura",tem)
        maks("predkosc_wiatru",pr)
        maks("wilgotnosc_wzgledna",wil)
        maks("suma_opadu",sum)
        maks("cisnienie",cis)

    print("największa temperatura to",tem['temperatura'],"jest ona w",tem['stacja'])
    print("największa prędkość wiatru to",pr['predkosc_wiatru'],"jest ona w",pr['stacja'])
    print("największa wilgotność względna to",wil['wilgotnosc_wzgledna'],"jest ona w",wil['stacja'])
    print("największa suma opadów to",sum['suma_opadu'],"jest ona w",sum['stacja'])
    print("największe ciśnienie to",cis['cisnienie'],"jest ono w",cis['stacja'])
    print('\n')

    for place in places:
        min("temperatura",tem)
        min("predkosc_wiatru",pr)
        min("wilgotnosc_wzgledna",wil)
        min("suma_opadu",sum)
        min("cisnienie",cis)
    
    print("najmniejsza temperatura to",tem['temperatura'],"jest ona w",tem['stacja'])
    print("najmniejsza prędkość wiatru to",pr['predkosc_wiatru'],"jest ona w",pr['stacja'])
    print("najmniejsza wilgotność względna to",wil['wilgotnosc_wzgledna'],"jest ona w",wil['stacja'])
    print("najmniejsza suma opadów to",sum['suma_opadu'],"jest ona w",sum['stacja'])
    print("najmniejsze ciśnienie to",cis['cisnienie'],"jest ono w",cis['stacja'])