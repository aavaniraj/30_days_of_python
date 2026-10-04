# Day 5

# Level 1

# Task 1
empty_list = []
print(empty_list)

# Task 2
items = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
print(items)

# Task 3
print(len(items))

# Task 4
print(items[0], items[len(items) // 2], items[-1])

# Task 5
mixed_data_types = ['Aavani Raj', 18, 1.75, 'Single', 'Panoor, India']
print(mixed_data_types)

# Task 6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Task 7
print(it_companies)

# Task 8
print(len(it_companies))

# Task 9
print(it_companies[0], it_companies[len(it_companies) // 2], it_companies[-1])

# Task 10
it_companies[0] = 'Meta'
print(it_companies)

# Task 11
it_companies.append('Twitter')
print(it_companies)

# Task 12
it_companies.insert(len(it_companies) // 2, 'Tesla')
print(it_companies)

# Task 13
it_companies[1] = it_companies[1].upper()
print(it_companies)

# Task 14
print('#; '.join(it_companies))

# Task 15
print('Apple' in it_companies)

# Task 16
it_companies.sort()
print(it_companies)

# Task 17
it_companies.reverse()
print(it_companies)

# Task 18
print(it_companies[:3])

# Task 19
print(it_companies[-3:])

# Task 20
mid_idx = len(it_companies) // 2
print(it_companies[mid_idx:mid_idx + 1])

# Task 21
it_companies.pop(0)
print(it_companies)

# Task 22
it_companies.pop(len(it_companies) // 2)
print(it_companies)

# Task 23
it_companies.pop()
print(it_companies)

# Task 24
it_companies.clear()
print(it_companies)

# Task 25
del it_companies

# Task 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# Task 27
full_stack_copy = full_stack.copy()
idx = full_stack_copy.index('Redux')
full_stack_copy.insert(idx + 1, 'Python')
full_stack_copy.insert(idx + 2, 'SQL')
print(full_stack_copy)


# Level 2

# Task 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("Min:", min(ages), "Max:", max(ages))

ages.append(min(ages))
ages.append(max(ages))
ages.sort()

n = len(ages)
median = (ages[n // 2 - 1] + ages[n // 2]) / 2 if n % 2 == 0 else ages[n // 2]
print("Median:", median)

avg = sum(ages) / len(ages)
print("Average:", avg)
print("Range:", max(ages) - min(ages))
print(abs(min(ages) - avg) == abs(max(ages) - avg))

# Task 2 & 3
countries = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
    'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain',
    'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan',
    'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria',
    'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde',
    'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros',
    'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba',
    'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic',
    'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea',
    'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The',
    'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea',
    'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India',
    'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan',
    'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South',
    'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia',
    'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar',
    'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania',
    'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco',
    'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand',
    'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama',
    'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal',
    'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia',
    'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia',
    'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore',
    'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain',
    'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria',
    'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga',
    'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda',
    'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay',
    'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen',
    'Zambia', 'Zimbabwe'
]

total = len(countries)
print("Middle:", countries[total // 2])
half = (total + 1) // 2
first_half = countries[:half]
second_half = countries[half:]
print("Divided:", len(first_half), len(second_half))

# Task 4
first, second, third, *scandic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(first, second, third, scandic)
