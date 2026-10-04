# Day 2: 30 Days of python programming

# Level 1

first_name = "Aavani"
last_name = "Raj"
full_name = "Aavani Raj"
country = "India"
city = "Panoor"
age = 18
year = 2026
is_married = False
is_true = True
is_light_on = True
school = "KKVMHSS PANOOR"

a, b, c = 10, 20, 30


# Level 2

# Task 1
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(school))

# Task 2
print(len(first_name))

# Task 3
print(len(first_name) == len(last_name))

# Task 4 - 11
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

# Task 12
import math

radius = 30
area_of_circle = math.pi * radius ** 2
circum_of_circle = 2 * math.pi * radius
print(area_of_circle)
print(circum_of_circle)

user_radius = float(input("Enter radius: "))
print(math.pi * user_radius ** 2)

# Task 13
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
country = input("Enter country: ")
age = int(input("Enter age: "))

# Task 14
help('keywords')
