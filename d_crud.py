import json_service as json_service
db = 'hospital.json'

def get_all_departaments():
    db = json_service.get_database()

    return db["departaments"]

def get_departament_by_id(id):
    db = json_service.get_database()
    for elem in db["departaments"]:
        if elem["id"] == id:
               return elem

    return {"message": f"Элемент с {id} не найден"}

def create_one(departament):
    db = json_service.get_database()

    last_departament_id = get_all_departaments()[-1]["id"]
    db["departaments"].append({"id": last_departament_id + 1, **departament})

    json_service.set_database(db)

def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["departaments"]):
        if elem["id"] == id:
            candidate = db["departaments"].pop(i)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {id} не найден"}

def update_one_by_id(departament_id, updates):
    db = json_service.get_database()

    for i, elem in enumerate(db["patients"]):
        if elem["id"] == departament_id:
            elem.update(updates)
            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с ID {departament_id} не найден"}

