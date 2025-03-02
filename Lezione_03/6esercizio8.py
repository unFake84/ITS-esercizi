from typing import Any

domestic: dict[str, Any] = {
    "race": "cat",
      "name": "Pino",
        "features": "pig",
          "legs": 4,
}

domestic1: dict[str, Any] = {
    "race": "Human",
      "name": "Dioni",
        "features": "gamer",
          "legs": 3,
}

domestic2: dict[str, Any] = {
    "race": "human",
      "name": "Fede",
        "features": "Uccia",
          "legs": 2
}

pet: list[Any] = [domestic, domestic1, domestic2]
print(pet)

for i in pet:
    
    if domestic['legs'] == 4:
        
        frase1: list[Any] = f"This animal that looks like a {i['race']}"

print(frase1)