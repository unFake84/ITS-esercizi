from typing import Any

info: dict[str, Any] = {
    "first_name": "Dioni",
      "last_name": "Manon",
        "age": 40,
          "city": "Rome",
}

info2: dict[str, Any] = {
    "first_name": "Pino",
      "last_name": "Maial",
        "age": 9,
          "city": "Myhouse"
}

info3: dict[str, Any] = {
    "first_name": "Fede",
      "last_name": "Uccia",
        "age": 38,
          "city": "Rome",
}

people: list[Any] = []

people.append(info)
people.append(info2)
people.append(info3)

print("-----------------------------------------------------------------------")

for i in people:

    frase: list[Any] = f"{i['first_name']} ha {i['age']} anni e vive a {i['city']}."
    print(frase)

print("-----------------------------------------------------------------------")