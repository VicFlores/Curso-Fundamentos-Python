
numbers = [1,2,3,4,5]

print(numbers)

numbers[-1] = 12

print(numbers)

numbers.append(500)

print(numbers)

numbers.insert(2, 55)

print(numbers)

numbers.insert(5, "Vic")

print(numbers)

task = ["Task1", "Task2", "Task3"]

newList = task + numbers

print(newList)

index = newList.index("Task1")

print(newList[index])

newList.remove("Task1")

print(newList)

newList.pop()

print(newList)

newList.pop(6)

print(newList)

newList.reverse()

print(newList)

numbers = [9,8,7,6,5]
vocals = ["u", "o", "i", "e", "a"]

numbers.sort()
vocals.sort()

print(numbers)
print(vocals)