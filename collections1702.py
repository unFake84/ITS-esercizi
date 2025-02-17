mydict: dict = {"key1": "Value1", "key2": "value2"}

for key in mydict:

    print(key)

for key in mydict:

    print(mydict[key])

for keys, values in mydict.items(): # .items()-> [(key1,value1), (key2,value2)]

    print(f"chiave: {keys}, valore: {values}")
