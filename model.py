import json

def load_json():
    with open("db.json") as f:
        return json.load(f)


def save_json():
    with open("db.json", "w") as f:
        return json.dump(db, f)


db = load_json()


def find_index(json_index):
    for i, dic in enumerate(db):
        if dic['id'] == json_index:
            return i
    return -1
