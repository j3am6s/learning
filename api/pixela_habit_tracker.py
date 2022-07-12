import requests
import os

### CREATE PIXELA ACCOUNT ###

user_parameters = {
    "token": os.environ.get("token"),
    "username": os.environ.get("username"),
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

pixela_endpoint = "https://pixe.la/v1/users"

user = requests.post(url=pixela_endpoint, json=user_parameters)
print(user.text) #--> {"message":"Success. Let's visit https://pixe.la/@alexthecaterpillar , it is your profile page!","isSuccess":true}


### CREATE GRAPH ###

graph_configuration = {
    "id": "graph1",
    "name": "mcdo",
    "unit": "hours",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": user_parameters["token"]
}

graph_endpoint = f"{pixela_endpoint}/{user_parameters['username']}/graphs"

graph = requests.post(url=graph_endpoint, json=graph_configuration, headers=headers)
print(graph.text)

# see graph online --> https://pixe.la/v1/users/alexthecaterpillar/graphs/graph1.html


### CREATE PIXEL ###

import datetime as dt

now = dt.datetime.now()
today = now.strftime("%Y%m%d")

pixel_parameters = {
    "date": today,
    "quantity": "3",
}

pixel_endpoint = f"{pixela_endpoint}/{user_parameters['username']}/graphs/{graph_configuration['id']}"

pixel = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=headers)
print(pixel.text)


### UPDATE PIXEL ###

update_parameters = {
    "quantity": "4"
}

update_endpoint = f"{pixela_endpoint}/{user_parameters['username']}/graphs/{graph_configuration['id']}/{today}"

update = requests.puzt(url=update_endpoint, json=update_parameters, headers=headers)
print(update.text)


### DELETE PIXEL ###

delete = requests.delete(url=update_endpoint, headers=headers)
print(delete.text)
