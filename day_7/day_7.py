# Day 7

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


# Level 1

# Task 1
print(len(it_companies))

# Task 2
it_companies.add('Twitter')
print(it_companies)

# Task 3
it_companies.update(['LinkedIn', 'Netflix', 'Spotify'])
print(it_companies)

# Task 4
it_companies.remove('Twitter')
print(it_companies)

# Task 5
# remove() raises KeyError if not found, discard() does not raise error


# Level 2

# Task 1
print(A.union(B))

# Task 2
print(A.intersection(B))

# Task 3
print(A.issubset(B))

# Task 4
print(A.isdisjoint(B))

# Task 5
print(A.union(B))
print(B.union(A))

# Task 6
print(A.symmetric_difference(B))

# Task 7
del A
del B


# Level 3

# Task 1
age_set = set(age)
print(len(age))
print(len(age_set))
print(len(age) > len(age_set))

# Task 2
# string: immutable sequence
# list: mutable ordered collection
# tuple: immutable ordered collection
# set: mutable unordered unique collection

# Task 3
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.replace('.', '').split()
print(len(set(words)))
