import json_service as json_service
db = 'hospital.json'
def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["patients"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["patients"]


def update_one_by_id(patient_id, updates):
    db = json_service.get_database()

    for i, elem in enumerate(db["patients"]):
        if elem["id"] == patient_id:
            elem.update(updates)
            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с ID {patient_id} не найден"}


def delete_patient_by_id(id):
    db = json_service.get_database()

    for i, patient in enumerate(db["patients"]):
        if patient["id"] == id:
            deleted_patient = db["patients"].pop(i)
            json_service.set_database(db)

            return deleted_patient

    return {"message": f"Пациент с идентификатором {id} не найден"}


def create_one(patient):
    db = json_service.get_database()

    last_patient_id = get_all()[-1]["id"]
    db["patients"].append({"id": last_patient_id + 1, **patient})

    json_service.set_database(db)




