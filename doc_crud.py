import json_service as json_service
db = 'hospital.json'

def get_all_doctors():
    db = json_service.get_database()

    return db["doctors"]

def get_doctor_by_id(id):
    db = json_service.get_database()
    for elem in db["doctors"]:
        if elem["id"] == id:
               return elem

    return {"message": f"Элемент с {id} не найден"}

def create_doctors(doctor):
    db = json_service.get_database()

    last_doctor_id = get_all_doctors()[-1]["id"]
    db["doctors"].append({"id": last_doctor_id + 1, **doctor})

    json_service.set_database(db)

def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["doctors"]):
        if elem["id"] == id:
            candidate = db["doctors"].pop(i)
            json_service.set_database(db)
            return candidate

    return {"message": f"Элемент с {id} не найден"}

def update_one_by_id(doctor_id, updates):
    db = json_service.get_database()

    for i, elem in enumerate(db["doctors"]):
        if elem["id"] == doctor_id:
            elem.update(updates)
            json_service.set_database(db)
            return elem
    return {"message": f"Элемент с ID {doctor_id} не найден"}