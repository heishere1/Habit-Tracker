
def greet(name):
    print("Hello, hello! ", name)
    print("Your result:")

age = int(input("Your age:"))
name1 = str(input("Your name:"))
if age < 18:
    greet(name1)
    print("You are a minor.")
elif age == 18:
    greet(name1)
    print("You are exactly 18.")
else:
    greet(name1)
    print("You are an adult.")
    


