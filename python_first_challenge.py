name = input("What is your name? ")
age = input("How old are you? ")
print("Hello, " + name + ", you are " + age + " years old!")

age = int(age)

if age < 18:
    print("You are a minor")
else:
    print("You're an adult")


fruits = ["banana", "apple", "strawberry"]
print(fruits)
print(fruits[0])

fruits[0] = "watermelon"
print(fruits)  # Output: ['watermelon', 'apple', 'strawberry']

for eachFruit in fruits:
  print(eachFruit) # for loop that prints each thing in a list

fruits.append("melon")
print(fruits)  # Output: ['watermelon', 'apple', 'strawberry', 'melon']

"melon" in fruits #Use in to check if a thing is in a list

child = {
  "name": "nino",
  "age" : 16,
  "occupation" : "student",
}
print(child["age"])
child["email"] = "nino@hotmail.com"

def greet(name, age): #define greet with two things inside
  print(f"Hello, {name}, you are {age} years old") #define the greet will do
greet("nino", 16) #use greet replacing "name" and "age"

#The following is the challenge
movies = ["madagascar", "avengers", "ratatoullie", "spirited away", "catch me if you can"]
for eachMovie in movies:
  print(eachMovie)
userMovie = input("What movie do you like?")
movies.append(userMovie)
print(movies)
userName = input("What is your name?")
userAge = input("How old are you?") #if change this to "int" I got an error before,
#but when I use it in a function the "int" doesn't matter. Although I would rather
#change it when I need the "int"
def greet(name, age):
  print(f"Hello, {name}, you are {age} years old.")
greet(userName, userAge)

#Tuples: inmmutable, cannot modify it, similar to a list
# coordinates = (10, 20, 30, 40)
# print(coordinates[0]) 

#Sets: doesn't allow duplicates, cannot access with using index
numbers = {1, 2, 3, 4, 5, 6, 8, 8,}
print(numbers[0])

#Can import modules to use their functionalities
import math
print(math.sqrt(81))

#Challenge: Create a tuple with three values (e.g., coordinates like x, y, z).
#Create a set with some random numbers, including duplicates. Print the set to show that duplicates are removed.
#Import the random module and use it to generate a random number between 1 and 10. Print the random number.

coordinates = (1, 3, 4)
randomNumbers = {1, 2, 3, 3}
print(randomNumbers)
import random
print(random.randint(1, 10)) #Random number between 1-10

