
numbers = (1,2,3,4,5)
customList = ["a", "b", "c"]
strings = ("Vic", "Vanessa", "Madeleyne")

print(type(numbers))
print(type(strings))

print(numbers[0])
print(numbers[-1])
print(strings[0])
print(strings[-1])
print("index",numbers.index(2))
print("index",strings.index("Madeleyne"))
print("count", numbers.count(numbers))
print("count", strings.count("Vic"))

convertTuple = tuple(customList)

print(customList)
print(convertTuple)
