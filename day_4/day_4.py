# Day 4

# Task 1
print(' '.join(['Thirty', 'Days', 'Of', 'Python']))

# Task 2
print(' '.join(['Coding', 'For', 'All']))

# Task 3
company = "Coding For All"

# Task 4
print(company)

# Task 5
print(len(company))

# Task 6
print(company.upper())

# Task 7
print(company.lower())

# Task 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Task 9
print(company.split()[0])

# Task 10
print(company.find('Coding'))

# Task 11
print(company.replace('Coding', 'Python'))

# Task 12
print("Python for Everyone".replace('Everyone', 'All'))

# Task 13
print(company.split(' '))

# Task 14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', '))

# Task 15
print(company[0])

# Task 16
print(len(company) - 1)

# Task 17
print(company[10])

# Task 18
print(''.join([w[0] for w in 'Python For Everyone'.split()]))

# Task 19
print(''.join([w[0] for w in company.split()]))

# Task 20
print(company.index('C'))

# Task 21
print(company.index('F'))

# Task 22
print("Coding For All People".rfind('l'))

# Task 23
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

# Task 24
print(sentence.rindex('because'))

# Task 25
start = sentence.find('because')
end = sentence.rindex('because') + len('because')
print(sentence[start:end])

# Task 26
print(sentence.find('because'))

# Task 27
print(sentence[start:end])

# Task 28
print(company.startswith('Coding'))

# Task 29
print(company.endswith('coding'))

# Task 30
print('   Coding For All      '.strip())

# Task 31
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# Task 32
print(' # '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

# Task 33
print("I am enjoying this challenge.\nI just wonder what is next.")

# Task 34
print("Name\tAge\tCountry\tCity")
print("Aavani\t18\tIndia\tPanoor")

# Task 35
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {int(area)} meters square.")

# Task 36
a, b = 8, 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
