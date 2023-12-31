## База данных

### CRUD-операции с сущностями

В программе доступны следующие CRUD-операции с сущностями в базе данных:

#### Создание (Create)

- Прежде чем выполнить операцию создания, база данных выглядит следующим образом:
  ["patients": [
        {
            "id": 1,
            "name": "Абдул Чичиков",
            "age": 34,
            "contacts": {
                "email": "Abdul@example.com",
                "phone": "+1234567890"
            },
            "hospital_room_id": 1
        },
        {
            "id": 2,
            "name": "Яблоко Рум",
            "age": 19,
            "contacts": {
                "email": "apple@example.com",
                "phone": "+0987654321"
            },
            "hospital_room_id": 2
        },
        {
            "id": 3,
            "name": "Арсений Дота2",
            "age": 48,
            "contacts": {
                "email": "ArsDOTA2@example.com",
                "phone": "+5678901234"
            },
            "hospital_room_id": 3]


- После выполнения операции создания сущности, база данных выглядит следующим образом:
  ["patients": [
        {
            "id": 1,
            "name": "Абдул Чичиков",
            "age": 34,
            "contacts": {
                "email": "Abdul@example.com",
                "phone": "+1234567890"
            },
            "hospital_room_id": 1
        },
        {
            "id": 2,
            "name": "Яблоко Рум",
            "age": 19,
            "contacts": {
                "email": "apple@example.com",
                "phone": "+0987654321"
            },
            "hospital_room_id": 2
        },
        {
            "id": 3,
            "name": "Арсений Дота2",
            "age": 48,
            "contacts": {
                "email": "ArsDOTA2@example.com",
                "phone": "+5678901234"
            },
            "hospital_room_id": 3
        },
        {
            "id": 4,
            "name": "лох лохович",
            "age": 16,
            "contacts": {
                "email": "loooh@gmail.com",
                "phone": "130322331343"
            },
            "hospital_room_id": 1
        },
        {
            "id": 5,
            "name": "Привет",
            "age": 12,
            "contacts": {
                "email": "priv@gmail.com",
                "phone": "1345435"
            },
            "hospital_room_id": 3
        }
    ],]

#### Чтение (Read)

- [При выборе в меню можно вывести либо все сущности, либо конкретную сущнусть]

- [Пример вывода всех сущностей  {'id': 1, 'name': 'Хирургическое отделение', 'doctor_id': [1]}, {'id': 2, 'name': 'Неврологическое отделение', 'doctor_id': [2]}, {'id': 3, 'name': 'Терапевтическое отделение', 'doctor_id': [3]}]
- [Пример вывода конкретной сущности {'id': 3, 'name': 'Терапевтическое отделение', 'doctor_id': [3]}]

#### Обновление (Update)

- Прежде чем выполнить операцию обновления, база данных выглядит следующим образом:
  [Описание текущего состояния базы данных"doctors": [
        {
            "id": 1,
            "name": "Врач",
            "contacts": {
                "email": "JoJo@example.com",
                "phone": "+88005553535"
            }
        },
        {
            "id": 2,
            "name": "Джонатан Джостар",
            "contacts": {
                "email": "JoJo@example.com",
                "phone": "+88005553535"
            }
        },
        {
            "id": 3,
            "name": "Баталфилд Овервотч",
            "contacts": {
                "email": "BatOver@example.com",
                "phone": "+3344556677"
            }
        },
        {
            "id": 4,
            "name": "Баталфилд Овервотч",
            "contacts": {
                "email": "BatOver@example.com",
                "phone": "+3344556677"
            }
        }
    ],]


- После выполнения операции обновления, база данных выглядит следующим образом(Обновлено имя у пациента под 3 id):
  ["doctors": [
        {
            "id": 1,
            "name": "Врач",
            "contacts": {
                "email": "JoJo@example.com",
                "phone": "+88005553535"
            }
        },
        {
            "id": 2,
            "name": "Джонатан Джостар",
            "contacts": {
                "email": "JoJo@example.com",
                "phone": "+88005553535"
            }
        },
        {
            "id": 3,
            "name": "Доктор Кто",
            "contacts": {
                "email": "BatOver@example.com",
                "phone": "+3344556677"
            }
        },
        {
            "id": 4,
            "name": "Баталфилд Овервотч",
            "contacts": {
                "email": "BatOver@example.com",
                "phone": "+3344556677"
            }
        }
    ],]

#### Удаление (Delete)

- Прежде чем выполнить операцию удаления, база данных выглядит следующим образом:
  ["departaments": [
        {
            "id": 1,
            "name": "Хирургическое отделение",
            "doctor_id": [
                1
            ]
        },
        {
            "id": 2,
            "name": "Неврологическое отделение",
            "doctor_id": [
                2
            ]
        },
        {
            "id": 3,
            "name": "Терапевтическое отделение",
            "doctor_id": [
                3
            ]
        },
        {
            "id": 4,
            "name": "ызхаоы",
            "doctor_id": [
                4
            ]
        }
    ]]


- После выполнения операции удаления, база данных выглядит следующим образом:
  ["departaments": [
        {
            "id": 1,
            "name": "Хирургическое отделение",
            "doctor_id": [
                1
            ]
        },
        {
            "id": 2,
            "name": "Неврологическое отделение",
            "doctor_id": [
                2
            ]
        },
        {
            "id": 3,
            "name": "Терапевтическое отделение",
            "doctor_id": [
                3
            ]
        }
    ]]

### Проверка айдишников при добавлении и обновлении

-При добавлении и обновлении сущностей, программа проверяет валидность айдишников и обеспечивает их уникальность.
[При выборе несуществующего id программа выдаст ошибку, например (Врач с указанным идентификатором не найден), а так же есть проверка на занятость id в других сущностях, например (Врач уже связан с другим отделением.)]]