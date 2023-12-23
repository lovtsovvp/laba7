import json
db = 'hospital.json'

def get_database():
    with open("hospital.json", encoding="utf-8") as hospital_file:
        return json.load(hospital_file)

def set_database(db):
    with open("hospital.json", "w", encoding="utf-8") as hospital_file:
        json.dump(db, hospital_file, ensure_ascii=False, indent=4)