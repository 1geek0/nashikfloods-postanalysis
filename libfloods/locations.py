import os

from libfloods.mongo import db

# locations = [
#     {"name": "Panchavati", "lat": 20.0074922, "long": 73.7841631, "z": 15, "aliases": []},
#     {"name": "Tapovan", "lat": 20.0007721, "long": 73.8099421, "z": 17, "aliases": []},
#     {"name": "Ekhlahre", "lat": 19.9680294, "long": 73.8714403, "z": 14, "aliases": []},
#     {"name": "Adgaon", "lat": 20.0375599, "long": 73.8326202, "z": 14, "aliases": []},
#     {"name": "New Adgaon Naka", "lat": 20.0105116, "long": 73.7982236, "z": 15, "aliases": ["Nawa Adgaon Naka"]},
#     {"name": "Old Adgaon Naka", "lat": 20.0061983, "long": 73.8125035, "z": 17, "aliases": ["Juna Adgaon Naka"]},
#     {"name": "Hirawadi", "lat": 20.0194935, "long": 73.8076691, "z": 16, "aliases": []},
#     {"name": "Ramkund", "lat": 20.0080157, "long": 73.790119, "z": 17, "aliases": ["Ram Ghat", "Ganga Ghat"]},
#     {"name": "Dwarka", "lat": 20.0014582, "long": 73.8015955, "z": 17, "aliases": []},
#     {"name": "Kathe Galli", "lat": 19.993239, "long": 73.8005628, "z": 17, "aliases": []},
#     {"name": "Shivaji Nagar", "lat": 20.008117, "long": 73.7740386, "z": 16, "aliases": []},
#     {"name": "Bodhle Nagar", "lat": 19.9825543, "long": 73.8042289, "z": 17, "aliases": []},
#     {"name": "Deepali Nagar", "lat": 19.9822783, "long": 73.7795517, "z": 16, "aliases": []},
#     {"name": "Upnagar", "lat": 19.9733393, "long": 73.817985, "z": 16, "aliases": []},
#     {"name": "Tagore Nagar", "lat": 19.9749196, "long": 73.8017915, "z": 16, "aliases": []},
#     {"name": "DGP Nagar", "lat": 19.9711125, "long": 73.7454148, "z": 18, "aliases": []},
#     {"name": "Nashik Road", "lat": 19.9701593, "long": 73.8118599, "z": 14, "aliases": []},
#     {"name": "Deolali", "lat": 19.9071551, "long": 73.7946612, "z": 13, "aliases": ["devlali"]},
#     {"name": "Deolali Camp", "lat": 19.8898025, "long": 73.8018113, "z": 14, "aliases": ["Devlali Camp"]},
#     {"name": "Gandhi Nagar", "lat": 19.9551334, "long": 73.7930464, "z": 14, "aliases": []},
#     {"name": "Mhasoba Nagar", "lat": 19.972724, "long": 73.7520587, "z": 18, "aliases": []},
#     {"name": "Pakhal Road", "lat": 19.9747034, "long": 73.7962669, "z": 17, "aliases": []},
#     {"name": "Bhabhanagar", "lat": 19.9885825, "long": 73.7868014, "z": 17, "aliases": ["Dr. Homi Bhabha Nagar"]},
#     {"name": "Mumbai Naka", "lat": 19.9877795, "long": 73.7756465, "z": 15, "aliases": ["Bombay Naka"]},
#     {"name": "Tidke Colony", "lat": 19.9917025, "long": 73.7698756, "z": 16, "aliases": []},
#     {"name": "Thakkar Bazar", "lat": 19.9986286, "long": 73.7781875, "z": 17, "aliases": ["New CBS"]},
#     {"name": "Ganjmal", "lat": 19.9960875, "long": 73.7849958, "z": 17, "aliases": []},
#     {"name": "CBS", "lat": 20.001213, "long": 73.7798995, "z": 17, "aliases": ["Old CBS"]},
#     {"name": "Gangapur Road", "lat": 20.0134183, "long": 73.7397737, "z": 17, "aliases": []},
#     {"name": "Sharanpur Road", "lat": 20.0026559, "long": 73.7699054, "z": 17, "aliases": []},
#     {"name": "College Road", "lat": 20.0058425, "long": 73.7610804, "z": 17, "aliases": []},
#     {"name": "Canada Corner", "lat": 20.0055553, "long": 73.7647021, "z": 16, "aliases": []},
#     {"name": "Ashok Stambh", "lat": 20.0063763, "long": 73.7828331, "z": 17, "aliases": []},
#     {"name": "Ravivar Karanja", "lat": 20.0067299, "long": 73.7871758, "z": 18, "aliases": ['RK']},
#     {"name": "Gangapur", "lat": 20.026061, "long": 73.6649613, "z": 17, "aliases": ['Gangapur Dam']},
#     {"name": "Ananadvali", "lat": 20.0133649, "long": 73.7310966, "z": 15, "aliases": []},
#     {"name": "Satpur", "lat": 20.0050269, "long": 73.7082489, "z": 14, "aliases": ["Satpur Colony"]},
#     {"name": "Satpur MIDC", "lat": 19.9988214, "long": 73.7231148, "z": 15, "aliases": ['MIDC Satpur']},
#     {"name": "Ambad", "lat": 20.3652124, "long": 73.6502007, "z": 18, "aliases": []},
#     {"name": "Ambad MIDC", "lat": 19.9531119, "long": 73.7166374, "z": 14, "aliases": ['MIDC Ambad']},
#     {"name": "Indira Nagar", "lat": 19.9742085, "long": 73.7770446, "z": 16, "aliases": []},
#     {"name": "CIDCO", "lat": 19.9726596, "long": 73.7543672, "z": 16, "aliases": []},
#     {"name": "Mahatma Nagar", "lat": 19.9981395, "long": 73.7486706, "z": 16, "aliases": []},
#     {"name": "Trimbak Road", "lat": 19.9909497, "long": 73.7320712, "z": 17,
#      "aliases": ['Trambak Road, Tryambak Road']},
#     {"name": "Rane Nagar", "lat": 19.9629621, "long": 73.7671221, "z": 16, "aliases": []},
#     {"name": "Ashwin Nagar", "lat": 19.9612541, "long": 73.7565056, "z": 16, "aliases": []},
#     {"name": "Govind Nagar", "lat": 19.985628, "long": 73.7707567, "z": 16, "aliases": []},
#     {"name": "Wadala Naka", "lat": 19.9933489, "long": 73.7942183, "z": 18, "aliases": []},
#     {"name": "Bhadrakali", "lat": 20.000617, "long": 73.7869914, "z": 17, "aliases": []},
#     {"name": "Pathardi", "lat": 19.9492739, "long": 73.7479429, "z": 14, "aliases": []},
#     {"name": "Pathatdi Fata", "lat": 19.9492739, "long": 73.7479429, "z": 14, "aliases": ['Pathardi Phata']},
#     {"name": "Kamatwade", "lat": 19.973484, "long": 73.7442071, "z": 17, "aliases": []},
#     {"name": "Kazipura", "lat": 19.9979561, "long": 73.7913323, "z": 17, "aliases": []},
# ]
locations = db.locations.find({})
location_list = []
for item in locations:
    location_list.append(item['name'])


def checkPath(path):
    if not os.path.exists(path):
        os.makedirs(path)


def filecount(dir_name):
    return len([f for f in os.listdir(dir_name) if os.path.isfile(f)])
