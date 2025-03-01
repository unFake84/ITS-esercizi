from typing import Any

info: dict[str, Any] = {"first_name": "Dioni", "last_name": "Manon", "age": 40, "city": "Rome"}

print("-----------------------------------------------------------------------")

for keys, values in info.items():

    print(keys, values)
print("-----------------------------------------------------------------------")

value_key1: list[str] = info["first_name"]
print(value_key1)
print("-----------------------------------------------------------------------")

value_key2: list[str] = info["last_name"]
print(value_key2)
print("-----------------------------------------------------------------------")

value_key3: list[Any] = info["age"]
print(value_key3)
print("-----------------------------------------------------------------------")

print(info["age"])
print("-----------------------------------------------------------------------")

print(info["city"])
print("-----------------------------------------------------------------------")

print(f"My first name is {value_key1} and my last name is {value_key2}")
print("-----------------------------------------------------------------------")

value_key4: list[str] = info["city"]
print(f"I ve {value_key3} years old and im living in {value_key4}")
print("-----------------------------------------------------------------------")