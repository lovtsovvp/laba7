import json_service as json_service
db = 'hospital.json'

def get_all_hospital_room():
    db = json_service.get_database()

    return db["hospital_rooms"]

def get_hospital_room_by_id(id):
    db = json_service.get_database()
    for elem in db["hospital_rooms"]:
        if elem["id"] == id:
               return elem

    return {"message": f"Элемент с {id} не найден"}

def create_hospital_room(hospital_room):
    db = json_service.get_database()

    last_patient_id = get_all_hospital_room()[-1]["id"]
    db["hospital_rooms"].append({"id": last_patient_id + 1, **hospital_room})

    json_service.set_database(db)


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["hospital_rooms"]):
        if elem["id"] == id:
            candidate = db["hospital_rooms"].pop(i)
            json_service.set_database(db)
            return candidate

    return {"message": f"Элемент с id {id} не найден"}

def update_one_by_id(hospital_room_id, updates):
    db = json_service.get_database()

    for i, elem in enumerate(db["hospital_rooms"]):
        if elem["id"] == hospital_room_id:
            elem.update(updates)
            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с ID {hospital_room_id} не найден"}