import json
import requests

r=requests.get("https://jsonplaceholder.typicode.com/todos")
#print(r.status_code)
        
def good(tasks):
    goodtasks=dict()
    for entry in tasks:
        if entry["completed"]==True:
            try:
                goodtasks[entry["userId"]]+=1
            except KeyError:
                goodtasks[entry["userId"]]=1
    return goodtasks

def bad(tasks):
    badtasks=dict()
    for entry in tasks:
        if entry["completed"]==False:
            try:
                badtasks[entry["userId"]]+=1
            except KeyError:
                badtasks[entry["userId"]]=1
    return badtasks
    
try:
    tasks=r.json()
except json.decoder.JSONDecodeError:
    print("niepoprawny format")
else:
    comp=[]
    git=good(tasks)
    nott=bad(tasks)
    
    for i in range(1,11):
        if git[i]<nott[i]:
            comp.append(i)
    #print(comp)

r=requests.get("https://jsonplaceholder.typicode.com/users")
users=r.json()
for user in users:
    if user['id'] in comp:
        print(user['name'],"sie opierdziela")