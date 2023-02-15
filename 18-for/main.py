
for item in range(1,10):
    print("item #1: ",item)

list = [1,2,3,4,5,6,7,8]

for item in list:
    print("item #2: ",item)

customTuple = (1,2,3,4,5)

for item in customTuple:
    print("item #3: ",item)

product = {
    "name": "Vic",
    "lastname": "Flores",
    "age": 22
}

for value in product:
    print("value: ",value)

for key in product:
    print("key: ",product[key])

for key, products in product.items():
    print(key, "=>", value )

people = [
    {
    "name": "Vic",
    "lastname": "Flores",
    "age": 22
    },

    {
    "name": "Madeleyne",
    "lastname": "Cañas",
    "age": 24
    }
]

for person in people:
    print(person)

for person in people:
    print("name", person["name"])
    print("age", person["age"])