# Day 6

# Level 1

# Task 1
empty_tuple = ()
print(empty_tuple)

# Task 2
brothers = ('Amrith',)
sisters = ('Aavani',)
print(brothers, sisters)

# Task 3
siblings = sisters + brothers
print(siblings)

# Task 4
print(len(siblings))

# Task 5
family_members = siblings + ('Avani', 'Amrith')
print(family_members)


# Level 2

# Task 1
*siblings_unpacked, father, mother = family_members
print(siblings_unpacked, father, mother)

# Task 2
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
animal_products = ('milk', 'meat', 'butter', 'yoghurt')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# Task 3
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Task 4
mid = len(food_stuff_tp) // 2
print(food_stuff_tp[mid:mid + 1])

# Task 5
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])

# Task 6
del food_stuff_tp

# Task 7
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
