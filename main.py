import requests 
import json

api_key = ""

with open('api_key.txt','r') as f:
  for line in f:
    api_key = line
headers = {
  'X-Api-Key': api_key,
}
nr = requests.get('https://api.newrelic.com/v2/users.json', headers=headers)
nr_json = nr.json()

with open("gerado.json", "w") as f:
  json.dump(nr_json, f)
  print("Lista de users adquirida com sucesso")

emails = open("emails.txt", "w")
with emails as f:
  for cada in nr_json["users"]:
    emails.write(str(cada["email"])+";")

print("Emails dos users registrados no arquivo 'emails.txt'") 
