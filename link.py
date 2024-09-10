import json
import requests

r=requests.get("https://jsonplaceholder.typicode.com/todos")
#print(r.status_code)

def count_task_frequency(tasks):
    ctasks=dict()
    for entry in tasks:
        if(entry["completed"]==True):
            try:
                ctasks[entry["userId"]]+=1
            except KeyError:
                ctasks[entry["userId"]]=1
    return ctasks

def ger_users_with_top_completed_tasts(tasks):
    usersIdWithMaxCompletedAmountOfTasks=[]
    maxAmountofcompletedTask=max(tasks.values())
    #print(maxAmountofcompletedTask)
    for userId, numberOfcompletetTask in tasks.items():
        if(numberOfcompletetTask==maxAmountofcompletedTask):
            usersIdWithMaxCompletedAmountOfTasks.append(userId)
    return usersIdWithMaxCompletedAmountOfTasks
try:
    tasks=r.json()
    #print(tasks)
except json.decoder.JSONDecodeError:
    print("niepoprawny format")
else:
    tasks= count_task_frequency(tasks)
    #print(tasks)
    winner=ger_users_with_top_completed_tasts(tasks)
    #print(winner)

#sposób 1
#r=requests.get("https://jsonplaceholder.typicode.com/users")
#users=r.json()
#for user in users:
#    if user["id"] in winner:
#        print("wygrał/a",user['name'])

#sposób 2
#for UserId in winner:
#    r=requests.get("https://jsonplaceholder.typicode.com/users",params="id"+str(UserId))
 #   user=r.json()
  #  print("wygrał/a",user[0]['name'])

def change_list_into_conj_of_param(my_list, key="id"):

    conj_param = key + "="
    lastIteration = len(my_list)
    i = 0
    for item in my_list:
        i += 1
        if(i == lastIteration):
            conj_param += str(item)
        else:
            conj_param += str(item) + "&" + key + "="
    return conj_param

#conj_param = change_list_into_conj_of_param(winner, "id")

#print(conj_param)

#r = requests.get("https://jsonplaceholder.typicode.com/users", params=conj_param)

#users = r.json()

#for user in users:
#    print("Wręczamy puchar mistrza dyscypliny do uzytkownikow o imieniu: ", user["name"])