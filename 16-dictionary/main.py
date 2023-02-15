
dict = {}

print(type(dict))

dict = {
    "name": "Vic",
    "lastname": "Flores",
    "age": 22
}

print(dict)
print(len(dict))
print(dict["name"])
print(dict["age"])
print(dict.get("lastname"))
print(dict.get("valor no existente"))
print("name" in dict)
print("single" in dict)


person = {
    "name": "Vic",
    "lastname": "Flores",
    "age": 22,
    "langs": ["python", "go", "js"]
}

print(person)

person["langs"].append("ts")

print(person)

del person["age"]

print(person)

person.pop("lastname")

print(person)

print("keys")
print(person.keys())

print("values")
print(person.values())

