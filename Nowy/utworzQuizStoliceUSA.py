# Progam tworzy quiz wraz z pytaniami i odpowiedziami
# ułożonymi w losowej kolejności wraz z odpowiedziami.
import random
# To są dane quizu. Klucze to nazwy stanów, natomiast wartości to ich stolice.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'Kalifornia': 'Sacramento', 'Kolorado': 'Denver', 
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Floryda': 'Tallahassee', 
'Georgia': 'Atlanta', 'Hawaje': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 
'Topeka', 'Kentucky': 'Frankfort', 'Luizjana': 'Baton Rouge', 'Maine': 
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'Nowy Meksyk': 'Santa Fe', 'Nowy Jork': 'Albany', 'Karolina Północna':
'Raleigh', 'Dakota Północna': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma':
'Oklahoma City', 'Oregon': 'Salem', 'Pensylwania': 'Harrisburg',
'Rhode Island': 'Providence', 'Karolina Południowa': 'Columbia',
'Dakota Południowa': 'Pierre', 'Tennessee': 'Nashville', 'Teksas': 'Austin',
'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Wirginia': 'Richmond',
'Waszyngton': 'Olympia', 'Wirginia Zachodnia': 'Charleston', 'Wisconsin':
'Madison', 'Wyoming': 'Cheyenne'}
Items = list(capitals.items())
tab=[]
tab2=[]
with open('pytania.txt', 'w') as f:
    f.write('imie i naziwsko: '+'\n')
    f.write("data:"+'\n'+'\n')
    f.write("klasa:"+'\n'+'\n')
    f.write("quiz o stolicach stanów"+'\n'+'\n')

    for i in range(31):
        k=random.choice(list(capitals.keys()))
        if k not in tab:
            tab.append(k)
            f.write(str(i)+". jaka jest stolica stanu "+k+"\n"+'\n')

            for i in range(4):
                tab2.append(k)
                z=random.choice(list(capitals.values()))
                if z not in tab2:
                    tab2.append(z)
                if(len(tab2)==4):
                    random.shuffle(tab2)
        f.write('\n')

