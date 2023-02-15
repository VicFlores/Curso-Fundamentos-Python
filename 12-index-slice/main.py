text = "Vic sabe Golang"
size = len(text)

print(text, text[0])
print(text, text[1])
print(text, text[size - 1])
print(text, text[-1])

# slice

print(text[0:5])
print(text[0:7])
print(text[4:])
print(text[:])
print(text[3:6:2])