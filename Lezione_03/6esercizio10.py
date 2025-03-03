#from typing import Any
fav_numbers: dict[str, int] = {
    "A": [10, 100, 600],
      "B": [20, 200, 700],
        "C": [30, 300, 800,],
          "D": [40, 400, 900],
            "E": [50, 500,1],
}


for key, value in fav_numbers.items():

    print(f"The alphabet: {key}, like number\s: {value}.")


# lista: list[Any] = [fav_numbers]

# key_a: list[Any] = []
# key_b: list[Any] = []
# key_c: list[Any] = []
# key_d: list[Any] = []
# key_e: list[Any] = []

# for i in lista:

#     key_a.append(i['A'])
#     key_b.append(i['B'])
#     key_c.append(i['C'])
#     key_d.append(i['D'])
#     key_e.append(i['E'])

#     for k, v in fav_numbers.items():

#         # print(k)
#         # print(v)
#         print(f"The alphabetics {k}, have this numbers: {v}")