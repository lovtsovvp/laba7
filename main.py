from p_crud import *
from json_service import *
from room_crud import *
from d_crud import *
from doc_crud import *
db = 'hospital.json'
def main_menu():
 while True:
  print("\nГлавное меню:")
  print("1. Управление пациентами")
  print("2. Управление отделениями")
  print("3. Управление врачами")
  print("4. Управление палатами")
  choice = input("Введите номер опции: ")

  if choice == '1':
   while True:
    print("\nУправление данными пациентов:")
    print("1. Показать всех пациентов")
    print("2. Найти пациента по ID")
    print("3. Добавить пациента")
    print("4. Обновить информацию об пациенте")
    print("5. Удалить пациента")
    print("6. Выйти")

    choice = input("Введите номер опции: ")

    if choice == '1':
     patients = get_all()
     print(patients)
    elif choice == '2':
     while True:
      try:
       patient_id = int(input("Введите ID пациента: "))
       break
      except ValueError:
       print("Введите целое число.")
     patient = get_one_by_id(patient_id)
     print(patient)
    elif choice == '3':
     name = input("Введите имя пациента: ")
     while True:
      try:
       age = int(input("Введите возраст пациента: "))
       break
      except ValueError:
       print("Ошибка: Возраст должен быть числом.")

     while True:
      email = input("Введите почту пациента: ")
      if "@" in email:
       break
      else:
       print("Ошибка: Некорректный формат почты.")

     while True:
      phone = input("Введите номер телефона пациента: ")
      if phone.isdigit():
       break
      else:
       print("Ошибка: Номер телефона должен быть числом.")

     def check_room_availability(hospital_room_id):
      hospital_data = get_database()
      hospital_rooms = hospital_data["hospital_rooms"]
      for hospital_room in hospital_rooms:
       if hospital_room["id"] == hospital_room_id:
        return True
      return False

     while True:
      try:
       hospital_room_id = int(input("Введите id комнаты пациента: "))
       if check_room_availability(hospital_room_id):
        break
       else:
        print("Ошибка: Комната с указанным id не существует.")
      except ValueError:
       print("Ошибка: Id комнаты должен быть числом.")

     patient_data = {
      "name": name,
      "age": age,
      "contacts": {
       "email": email,
       "phone": phone
      },
      "hospital_room_id": hospital_room_id
     }
     create_one_p(patient_data)
    elif choice == '4':
     while True:
      try:
       patient_id = int(input("Введите ID пациента: "))
       break
      except ValueError:
       print("Введите целое число.")
     updates = {}

     print(
      "Выберите, что вы хотите обновить (1 - имя, 2 - возраст, 3 - номер телефона, 4 - почту, 5 - комнату): ")
     update_choice = input("Введите номер действия: ")
     if update_choice == '1':
      updates['name'] = input("Введите новое имя пациента: ")
     elif update_choice == '2':
      while True:
       try:
        updates['age'] = int(input("Введите новый возраст пациента: "))
        break
       except ValueError:
        print("Ошибка: Возраст должен быть числом.")
     elif update_choice == '3':
      while True:
       try:
        updates['phone'] = int(input("Введите новый номер телефона пациента: "))
        break
       except ValueError:
        print("Ошибка: Номер телефона должен быть числом.")
     elif update_choice == '4':
      while True:
       email = input("Введите новую почту пациента: ")
       if "@" in email:
        updates['email'] = email
        break
       else:
        print("Ошибка: Некорректный формат почты.")
     elif update_choice == '5':

      def checkroomavailability(hospital_room_id):
       hospitaldata = get_database()
       hospitalrooms = hospitaldata
       "hospital_rooms"
       for hospitalroom in hospitalrooms:
        if hospitalroom["id"] == hospital_room_id:
         return True
       return False

     while True:
      try:
       updates['hospitalroomid'] = input("Введите новый номер комнаты пациента: ")
       if checkroomavailability(hospital_room_id):
        break
       else:
        print("Ошибка: Комната с указанным id не существует.")
      except ValueError:
       print("Ошибка: Id комнаты должен быть числом.")
      else:
       print("Некорректный выбор.")
     result = update_one_by_id(hospital_room_id, updates)
     if "message" in result:
      print(result["message"])
     else:
      print(f"Данные пациента с ID {hospital_room_id} успешно обновлены.")
    elif choice == '5':
     while True:
       try:
        id = int(input("Введите ID пациента для удаления: "))
        break
       except ValueError:
        print("Введите целое число.")
     result = delete_patient_by_id(id)
     print(result)
    elif choice == '6':
     break
  elif choice == '2':

   while True:
    print("\nУправление данными отделений:")
    print("1. Показать все отделения")
    print("2. Найти отделение по ID")
    print("3. Добавить отделение")
    print("4. Удалить отделение")
    print("5. Обновить информацию об отделении")
    print("6. Выйти")

    choice = input("Введите номер опции: ")

    if choice == '1':
     departaments = get_all_departaments()
     print(departaments)

    elif choice == '2':
     while True:
      try:
       departament_id = int(input("Введите ID отделения: "))
       break
      except ValueError:
       print("Введите целое число.")
     departament = get_departament_by_id(departament_id)
     print(departament)

    elif choice == '3':
     def create_departament(departament_data):
      try:
       hospital_data = get_database()

       doctor_id = departament_data["doctor_id"]
       doctors = hospital_data["doctors"]

       doctor_exists = False
       for doctor in doctors:
        if doctor["id"] == doctor_id:
         doctor_exists = True
         break

       if not doctor_exists:
        print("Врач с указанным идентификатором не найден.")
        return

       departaments = hospital_data["departaments"]
       for department in departaments:
        if department["doctor_id"] == doctor_id:
         print("Врач уже связан с другим отделением.")
         return

       departaments.append(departament_data)

       set_database(hospital_data)

       print("Отделение успешно создано.")

      except ValueError:
       print("Произошла ошибка при создании отделения.")

     name = input("Введите название отделения: ")
     doctor_id = int(input("Введите id доктора: "))
     departament = {
      "name": name,
      "doctor_id": doctor_id
     }

     create_departament(departament)
    elif choice == '4':
     while True:
      try:
       id = int(input("Введите ID отделения для удаления: "))
       break
      except ValueError:
       print("Введите целое число.")
     result = delete_one_by_id(id)
     print(result)
    elif choice == '5':
     while True:
      try:
       doctor_id = int(input("Введите ID врача: "))
       break
      except ValueError:
       print("Введите целое число.")
     updates = {}

     print(
      "Выберите, что вы хотите обновить (1 - имя, 2 - номер телефона, 3 - почту): ")
     update_choice = input("Введите номер действия: ")
     if update_choice == '1':
      updates['name'] = input("Введите новое имя врача: ")
     elif update_choice == '2':
      while True:
       try:
        updates['phone'] = int(input("Введите новый номер телефона врача: "))
        break
       except ValueError:
        print("Ошибка: Номер телефона должен быть числом.")
     elif update_choice == '3':
      while True:
       email = input("Введите новую почту врача: ")
       if "@" in email and len(email)>1:
        updates['email'] = email
        break
       else:
        print("Ошибка: Некорректный формат почты.")
    elif choice == '6':
     print("Выход в главное меню.")
     break

  elif choice == ('3'):
   while True:
    print("\nУправление данными врачей:")
    print("1. Показать всех врачей")
    print("2. Найти врача по ID")
    print("3. Добавить врача")
    print("4. Удалить врача")
    print("5. Обновить данные врача")
    print("6. Выйти")

    choice = input("Выберите действие: ")
    if choice == "1":
     doctors = get_all_doctors()
     for doctor in doctors:
      print(doctor)
    elif choice == "2":
     doctor_id = input("Введите ID врача: ")
     found_doctor = get_doctor_by_id(doctor_id)
     print(found_doctor)
    elif choice == "3":
     name = input("Введите имя врача: ")
     while True:
      email = input("Введите почту врача: ")
      if "@" in email:
       break
      else:
       print("Ошибка: Некорректный формат почты.")
     while True:
      phone = input("Введите номер телефона врача: ")
      if phone.isdigit():
       break
      else:
       print("Ошибка: Номер телефона должен быть числом.")

     doctor_data = {
      "name": name,
      "contacts": {
       "email": email,
       "phone": phone,
      }
     }
     create_doctors(doctor_data)
    elif choice == "4":
     while True:
      try:
       id = int(input("Введите ID врача для удаления: "))
       break
      except ValueError:
       print("Введите целое число.")
     result = delete_one_by_id(id)
     print(result)
    elif choice == "5":
     while True:
      try:
       doctor_id = int(input("Введите id врача: "))
       break
      except ValueError:
       print("Ошибка: Id врача должен быть числом.")

     updates = {}
     print("Выберите, что вы хотите обновить (1 - имя, 2 - номер телефона, 3 - почту): ")
     update_choice = input("Введите номер действия: ")
     if update_choice == '1':
      updates['name'] = input("Введите новое имя врача: ")
     if update_choice == '2':
      while True:
       try:
        updates['phone'] = int(input("Введите новый номер телефона врача: "))
        break
       except ValueError:
        print("Ошибка: Номер телефона должен быть числом.")
     elif update_choice == '3':
      while True:
       email = input("Введите новую почту врача: ")
       if "@" in email:
        updates['email'] = email
        break
       else:
        print("Ошибка: Некорректный формат почты.")
     updated_doctor = update_doc_one_by_id(hospital_room_id, updates)
     if "message" in updated_doctor:
      print(updated_room["message"])
     else:
      print("Обновление прошло успешно.")
    elif choice == "6":
     print("Работа с врачами завершена.")
     break
    else:
     print("Некорректный выбор.")
  elif choice == '4':
     while True:
      print("\nУправление данными палат:")
      print("1. Показать все палаты")
      print("2. Найти палту по id")
      print("3. Добавить палату")
      print("4. удалить палату")
      print("5. Обновить данные палаты")
      print("6. Выйти")

      choice = input("Выберите пункт меню: ")

      if choice == "1":
       print(get_all_hospital_room())
      elif choice == "2":
       room_id = int(input("Введите id палаты: "))
       print(get_hospital_room_by_id(room_id))
      elif choice == "3":
       name = input("Введите название: ")

       def check_departament_availability(departament_id):
        hospital_data = json_service.get_database()
        departaments = hospital_data["departaments"]
        for departament in departaments:
         if departament["id"] == departament_id:
          return True
        return False
       while True:
        try:
         departament_id = int(input("Введите id  отделения: "))
         if check_departament_availability(departament_id):
          break
         else:
          print("Ошибка: Отделение с указанным id не существует.")
        except ValueError:
         print("Ошибка: Id отделения должен быть числом.")

       hospital_room = {
        "name": name,
        "departament_id": departament_id
       }
       print("Палата успешно создана.")

       create_hospital_room(hospital_room)
      elif choice == "4":
       id = int(input("Введите id палаты, которого нужно удалить: "))
       result = delete_one_by_id(id)
       print(result)
      elif choice == "5":
       def check_departament_availability(departament_id):
        hospital_data = json_service.get_database()
        departaments = hospital_data["departaments"]
        for departament in departaments:
         if departament["id"] == departament_id:
          return True
        return False

       while True:
        try:
         hospital_room_id = int(input("Введите id палаты: "))
         break
        except ValueError:
         print("Ошибка: Id палаты должен быть числом.")

        updates = {}
        print("Выберите, что вы хотите обновить (1 - имя, 2 - отделение): ")
        update_choice = input("Введите номер действия: ")
        if update_choice == '1':
         updates['name'] = input("Введите новое имя палаты: ")
        if update_choice == '2':
         while True:
          try:
           departament_id = int(input("Введите id нового отделения: "))
           if check_departament_availability(departament_id):
            updates['departament_id'] = departament_id
            break
           else:
            print("Ошибка: Отделение с указанным id не существует.")
          except ValueError:
           print("Ошибка: Id отделения должен быть числом.")

       if updates:
        updated_room = update_one_by_id(hospital_room_id, updates)
        if "message" in updated_room:
         print(updated_room["message"])
        else:
         print("Обновление прошло успешно.")
       else:
        print("Некорректный выбор.")
      elif choice == "6":
       print("Работа с палатами завершена.")
       break
  else:
    print("неверный ввод, пожалуйста, попробуйте снова.")
    input("нажмите enter для продолжения...")
    print("выход из программы.")
main_menu()