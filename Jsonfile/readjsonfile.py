
import json

with open("filejson.json") as f:

    data = json.load(f)


# for p in data['LoginPage']:
#     print('Name: ' + p["Username"])

for key, value in data.items():
    print (key)
    print (value)

for key, value in data.items():
    if key == "LoginPage":
        for value in data[key]:
            print(value["Username"])



        #print (key)
        #print(value)



