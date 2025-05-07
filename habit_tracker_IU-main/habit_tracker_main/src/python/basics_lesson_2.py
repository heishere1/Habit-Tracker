# Global variable declared at the top level of the program
x = 10

#def show_x():
    # This function can read the global variable without using 'global'
 #   print("x inside show_x() =", x)

#def modify_x():
 #   global x  # This tells Python we want to use the global x, not create a local one
  #  x = 20    # This will modify the global variable x
   # print("x inside modify_x() (after change) =", x)
#def print_local():
 #   x = 5  # Local variable inside function
 #   print("Inside function:", x) */

#print_local()
#print("Outside function:", x)

def print_local():
    x = 5  # Local variable inside function
    print("Inside function:", x)

print_local()
print("Outside function:", x)

import math
print(math.sqrt(16))
import datetime
print(datetime.date.today())  

age = int(input("Enter your age: "))
print("Next year you'll be", age + 1)

age = input("enter your age: ")
print("next year you'll be", age +1)

habits = []
def add_habit(habit_name):

    add_habit("Drink water")
    add_habit("Exercise")
print("Your habits:" , habits)

import csv
habits = []
while True:
    habit_name = input("exercise,excessive talking,too much eating,studying everyday (or  'q' to quit): ").strip()
    if habit_name.lower() == 'q' :
        break
    habits.append(habit_name)
with open('habit.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
writer.writerow(['Habit Name'])
