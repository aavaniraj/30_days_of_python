# Day 3

# Task 1
age = 18

# Task 2
height = 1.75

# Task 3
complex_number = 1 + 4j

# Task 4
base = float(input("Enter base: "))
triangle_height = float(input("Enter height: "))
print("The area of the triangle is", 0.5 * base * triangle_height)

# Task 5
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
print("The perimeter of the triangle is", side_a + side_b + side_c)

# Task 6
length = float(input("Enter length: "))
width = float(input("Enter width: "))
print("Area:", length * width)
print("Perimeter:", 2 * (length + width))

# Task 7
radius = float(input("Enter radius: "))
pi = 3.14
print("Area:", pi * radius * radius)
print("Circumference:", 2 * pi * radius)

# Task 8
slope_1 = 2
y_intercept_1 = -2
x_intercept_1 = 1
print("Slope:", slope_1, "y-intercept:", y_intercept_1, "x-intercept:", x_intercept_1)

# Task 9
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_2 = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Slope:", slope_2)
print("Euclidean distance:", distance)

# Task 10
print(slope_1 == slope_2)

# Task 11
for x in [-5, -4, -3, -2, -1, 0, 1]:
    y = x ** 2 + 6 * x + 9
    print(f"x={x}, y={y}")

# Task 12
print(len('python') != len('dragon'))

# Task 13
print('on' in 'python' and 'on' in 'dragon')

# Task 14
print('jargon' in "I hope this course is not full of jargon")

# Task 15
print('on' not in 'dragon' and 'on' not in 'python')

# Task 16
length_val = str(float(len('python')))
print(length_val)

# Task 17
num = 10
print(num % 2 == 0)

# Task 18
print(7 // 3 == int(2.7))

# Task 19
print(type('10') == type(10))

# Task 20
try:
    print(int('9.8') == 10)
except ValueError:
    print(int(float('9.8')) == 10)

# Task 21
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
print("Your weekly earning is", hours * rate)

# Task 22
years = int(input("Enter number of years you have lived: "))
print(f"You have lived for {years * 365 * 24 * 60 * 60} seconds.")

# Task 23
for i in range(1, 6):
    print(f"{i} 1 {i} {i ** 2} {i ** 3}")
