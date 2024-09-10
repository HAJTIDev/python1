import requests,json
r=requests.get("https://danepubliczne.imgw.pl/api/data/synop/station/lodz")
place=r.json()
print("temperatura",place['temperatura'])
print('predkosc wiatru',place['predkosc_wiatru'])
print("wilgotność",place['wilgotnosc_wzgledna'])
print("suma opadów",place['suma_opadu'])
print("ciśnienie",place['cisnienie'])
