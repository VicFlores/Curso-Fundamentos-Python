
text = "Soy Vic Flores y soy científico"

print("Golang" in text)
print("Vic Flores" in text)

if "Vic Flores" in text:
    print("Hola Vic")
else:
    print("Nothing")

size = len("love")
print("Size", size)

size = len(text)
print("Size", size)

print(text, text.upper())
print(text, text.lower())
print(text, text.count("a"))
print(text, text.swapcase())
print(text, text.startswith("Soy"))
print(text, text.endswith("científico"))
print(text, text.replace("Vic Flores", "Vic Escobar"))
print(text, text.isdigit())
print("345", "345".isdigit())