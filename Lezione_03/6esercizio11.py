from typing import Any

cities: dict[str, Any] = {
    "Rome": {
        "country": "Italy",
          "population": 2.752,
            "fact": "chaotic!"
              },
      "Salisburg": {
          "country": "Austria",
            "population": 154.211,
              "fact": "home of music"
                },
        "Home": {
            "country": "Uccland",
              "population": 3,
                "fact": "homy sweety homie"
                  }
}

i = 1

print("-----------------------------------------------------------------------")
for key, dict in cities.items():

    print(f"{i}){key}:\n")
    i += 1

    for under_key, values in dict.items():

        print(f"{under_key.title()} = {values}")
        
    print()    
    print(dict)
    print("-----------------------------------------------------------------------")

    