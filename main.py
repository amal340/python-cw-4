
def my_function():
    print ("My name is amal")

my_function()

def my_meal(food, drink = "Orange Juice"):
    print (f"I like to eat {food} while drinking {drink}")

my_meal("Sandwitchs")

def cube(number):
    return number**3

print (cube(3))

def by_three(number):
    if number%3==0:
        return cube(number)
    else:
        return False

print (by_three(1))