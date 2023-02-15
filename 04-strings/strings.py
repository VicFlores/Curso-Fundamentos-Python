
name = "Vic Ferman"
lastname = "Flores Escobar"
fullname = name + lastname
quote1 = "I'm VicFlores11"
quote2 = 'She said "Hello"'

print("Name:",name)
print("Lastname:",lastname)
print("Full Name", fullname)
print("Quote1", quote1)
print("Quote2", quote2)

# format

template1 = "Hello, Mi name is " + name + " and my lastname is " + lastname
template2 = "Hello, Mi name is {} and my lastname is {}".format(name, lastname)
template3 = f"Hello, Mi name is {name} and my lastname is {lastname}"

print("Template1:", template1)
print("Template2:", template2)
print("Template3:", template3)
