from pymongo import *

# Setup MongoDB
dbclient = MongoClient(host="ds139715.mlab.com", port=39715)
dbclient.nashikfloods.authenticate('nashikfloods', 'nashikfloods')
db = dbclient.nashikfloods


# def addHelp(location, people, food, water, rescue, contact, name):
#     db.insert(
#         {"location": location, "people": people, "food": food, "water": water, "rescue": rescue, "contact": contact,
#          "name": name})


def addLocation(location):
    db.locations.insert({
        'name': location['name'],
        'lat': location['lat'],
        'long': location['long'],
        'z': location['z'],
        'aliases': location['aliases']
    })
    print("Inserted " + location['name'])


def addPost(file):
    pass
