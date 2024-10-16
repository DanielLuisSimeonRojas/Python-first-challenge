name = input("What is your name? ")
age = (input("How old are you? "))
print("Hello, " + name + ", you are " + age + " years old!")

age = int(age)

if age < 18:
    print("You are a minor")
else:
    print("You're an adult")
