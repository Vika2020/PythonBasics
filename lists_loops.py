# # # # Chapter 4: Working with LIST
# # #
# # # states = ['New York', 'New Jersey', 'Connecticut', 'Virginia', 'California']
# # #
# # # # for variable in list_of_elements:
# # # #     repetitive code here
# # #
# # # for state in states:
# # #     print(f"Welcome to {state}!!")
# # #
# # #     print(f"Enjoy your trip {state.upper()}!!")
# # #
# # # # example
# # #
# # #
# # # pizzas = {'four cheese', 'vegetarian', 'pepperoni'}
# # # for pizza in pizzas:
# # #     print(f"I am going order {pizza} for dinner!")
# # # print('What can be batter than pizza?!')
# #
# #  # working with numbers
# # for num in range(5):
# #     print(f"My current number from range(5): {num}")
# # for num in range(3, 6):
# #     print(f"My current number from range(3,6): {num}")
#
# numbers = list(range(5))
# print(numbers)
#
# # print squares of numbers from 5 to 12
# for num in range(5,13):
#     print(num**2)
#
# squares = []
# for num in range(5, 13):
#     num_sqr = num ** 2
#     squares.append(num_sqr)
#     print(num_sqr)
#     print(squares)
#
# print(squares)

# numbers = [2, 54, 76, 3, 7, 56, 2]
# print(f"Min number from numbers : {min(numbers)}")
# print(f"Max number from numbers : {max(numbers)}")
# print(f"Sum number from numbers : {sum(numbers)}")

# name = "John Doe"
# print(name[5:])
#
# numbers = [2, 54, 76, 3, 7, 56, 2]
# print(numbers[3:])
# print(numbers[2:-2])

# numbers = [2, 54, 76, 3, 7, 56, 2]
# numbers_copy = numbers[:]
# print(numbers_copy)
#
# numbers_copy

# Ex. 4-10

# numbers = [2, 54, 76, 3, 7, 56, 2]
# print("The first three numbers in the list are:")
# for number in numbers[:3]:
#     print(number)

# my_pizza = ['four cheese', 'vegetarian', 'pepperoni']
# friends_pizza = my_pizza[:]
# print(my_pizza)
# print(friends_pizza)
# my_pizza.append('margarita')
# friends_pizza.append('artichoke')
# print(my_pizza)
# print(friends_pizza)


#
# foods = ('salad', 'meat', 'bread', 'dessert', 'drinks')
# for food in foods:
#     print(food.title())


# name = 'Victoriya'
# # for a in name:
# #     print(a)
#
#
# friends = ['vika', 'olya', 'saga', 'saida']
# print(friends[-1])
#
# for i in friends:
#     print(i)
#
# for i in range(len(friends)):
#     print(f"element on index {i} is {friends[i]}")

# pizzas = ['margarita', 'four cheese', 'vegetarian', 'pepperoni']
# print(pizzas)
# print(sorted(pizzas))
# print(sorted(pizzas, reverse=True))
# print(pizzas)
#
# pizzas.reverse()
# print(pizzas)
#
# pizzas.sort(reverse=True)
# print(pizzas)
#
# pizzas.count()
# print(pizzas)

#
# pizzas = ['four cheese', 'vegetarian', 'pepperoni']
# pizzas.pop(0)
# print(pizzas)
# pizzas.insert(2,'margarita')
# print(pizzas)
# pizzas.append('pineapple')
# print(pizzas)
# pizzas.remove('pineapple')
# print(pizzas)
# len(pizzas)
# print(pizzas)

# student1 = {'name': 'Vika', 'gpa': 4.0}
# student2 = {'name': 'Saida', 'gpa': 3.8}
#
# print(student1)
# print(student1['name'], student1['gpa'])


# num_1 = 18
# num_2 = 21
# num_1 > 18 and num_2 < 21


# list_of_students = ['Vika', 'Maxi', 'Steve', 'Sara']
# 'Vika' not in list_of_students
#
# 'Akobir' in list_of_students
#
# banned_users = ['Maria', 'Karl', 'Evan']
# if 'Karl' not in banned_users:
#     print('You can leave a comment')
# else:
#     print('You are not allowed to leave a comment')

# banned_users = ['Maria', 'Karl', 'Evan']
# user_1 = 'Evan'
# user_2 = 'Sara'
#
# if user_1 not in banned_users:
#     print(user_1.upper() + " , you can leave a comment." )
# else:
#     print(user_2.upper() + ", you are not allowed to write a comment!")


# Ex 5-1,2

# city = 'Paris'
# print("Is city == 'Paris'? I predict True.")
# print(city == 'Paris')
#
# print("Is city != 'Paris'? I predict False")
# print(city == 'Miami')

# age = 17
# if age >= 18:
#     print("You can vote!")
#     print("Have you registered to vote yet?")
# else:
#     print('Sorry, you cannot vote!')
#
# age = 66
# if age <4:
#     cost = 0
# elif age < 12:
#     cost = 5
# elif age >= 65:
#     cost = 8
# else:
#     cost = 12
# print("Your admission cost is $" + str(cost) + ".")

# =======  Fuzz - Buzz problem =======

# for i in range(3):
#     num = (int(input("Enter your number:")))
#     if num % 3 == 0 and num % 5 ==0:
#         print('FuzzBuzz')
#     elif num % 5 ==0:
#         print('Buzz')
#     elif num % 3 ==0:
#         print('Fuzz')
#
# rivers = {'nile': 'egypt', 'hudson': 'usa', 'volga': 'russia', 'mississippi': 'usa', 'thames': 'uk'}
#
# for river, country in rivers.items():
#     # if country == 'usa' or country == 'uk':
#     if country in ['usa', 'uk']:
#        print(f" The {river.upper()} runs through {country.upper()}")
#     else:
#        print(f"The {river.title()} runs through {country.title()}")
#
# print('Rivers are: ')
# for river in rivers.keys():
#         print('\t', river.title())
# print('Countries are:')
# for country in rivers.values():
#     if country in ['usa', 'uk']:
#         print('\t', country.upper())
#     else:
#         print('\t', country.title())

#
# cities = {'New York': {'country': 'USA', 'population': 8.4, 'fact': 'Big Apple'},
#            'Istanbul': {'country': 'Turkey', 'population': 15.52 , 'fact': 'Constatinople'},
#            'Moscow': {'country': 'Russia', 'population': 12.53, 'fact': 'Red Square'}}
#
# for city, info in cities.items():
#     # print(city)
#     # print(info)
#     print(f"{city} is very beautiful city in {info['country']}."
#           f"It has {info['population']} mln population and the city is also know as {info['fact']}.")

 # Ex. 5-3

# alien_color = 'green'
# if alien_color == 'green':
#     print('You just earned 5 points')
# elif alien_color == 'red':
#     print('You just earned 10 points')
# else:
#     print('You just earned 15 points')


# person_age = 5
# if person_age < 2:
#     print("This person is baby")
# elif person_age >= 2 and person_age < 4:
#     print("This person is toddler")
# elif person_age >= 4 and person_age < 13:
#     print("This person is kid")
# elif person_age >= 13  and person_age < 20:
#     print("This person is a teenager")
# elif person_age  >= 20 and person_age  < 65:
#     print("This person is an adult")
# else:
#     print("This person is an elder")

# fruits = ['apple', 'orange', 'banana']
# if 'apple' in fruits:
#     print('You really like apple')
# if 'orange' in fruits:
#     print('You really like orange')
# if 'banana' in fruits:
#     print('You really like bananas')

# ==== Dictionaries ====

#  creating dictionary and adding a new value #

# friend_1 = {'name': 'Oksi', 'age': '37', 'address': 'Richmond'}
# print(friend_1)
# friend_1['status'] = 'married'
# print(friend_1)
# friend_1['children'] = 2
# print(friend_1)
# print(friend_1['status'])

# ==== changing value ===

# friend_2 = {}
# friend_2['name'] = 'Akobir'
# friend_2['status'] = 'married'
# friend_2['kids'] = 1
# print(friend_2)
# friend_2['kids'] = 2
# print(friend_2)
# print("I know " + friend_2['name'] + " for many years. \nHe has " + str(friend_2['kids']) + " kids.")

# ==== delete value ===

# friend_1 = {'name': 'Oksi', 'age': '37', 'address': 'Richmond'}
# del friend_1['address']
# print(friend_1)
# friend_1['kids'] = 2
# print(friend_1['name'].upper() + " and her husband have " + str(friend_1['kids']) + " kids.")


# mama = {'first_name': 'Raisa', 'last_name': 'Dogbaeva', 'age': 71, 'city': 'Brooklyn'}
# print(mama['first_name'])
# print(mama['last_name'])
# print(mama['age'])
# print(mama['city'])

# fav_numbers = {'Vika': 14, 'mama': 18, 'papa': 16}
# print(fav_numbers)

# === looping through dictionary ===


# full_name = {'name': 'Vika', 'middle name': 'Ageevna', 'last name': 'Dogbaeva'}
# for key, value in full_name.items():
#     print("\nKey:" + key)
#     print("Value:" + value)


# fav_numbers = {'Vika': 14, 'mama': 18, 'papa': 16}
# fav_numbers['bro'] = 17
# print(fav_numbers)

# for name, number in fav_numbers.items():
#     print("\nName:" + name)
#     print("Number:" + str(number))

# for name in fav_numbers:
#     print(name.title())
#
# fav_numbers = {'Vika': 14, 'mama': 18, 'papa': 16}
# for name in fav_numbers.keys():
#     print(name.title())

# fav_numbers = {'vika': 14, 'papa': 16, 'mama': 18}
# print(fav_numbers)
# # family = ['mama', 'papa']
# # for name in fav_numbers.keys():
# #     print(name.upper())
# #
# #     if name in family:
# #        print("\nHello " + name.title() + ". " "\nI see your favorite number is " + str(fav_numbers[name]) + ".")
# # if 'bro' not in fav_numbers.keys():
# #     print("Bro, what's your favorite number?")

# sort keys
# for name in sorted(fav_numbers.keys()):
#     print(name.title() + " , thank you for sharing your favorite number!")

# fav_numbers = {'Vika': 14, 'mama': 18, 'papa': 16}
# print("Your favorite numbers are:")
# for number in fav_numbers.values():
#     print(number)

# Ex. 6-5

rivers = {'Volga': 'Russia', 'Nile': 'Africa', 'Amazon': 'Africa'}
# for key, value in rivers.items():
#     print("The " + (key) + " runs trough " + (value) + ".")
#
# for key in rivers:
#     print(key)
# for value in rivers.values():
#     print(value)

# === Putting a dictionary inside a list ===

# apt_1 = {'location': 'Brooklyn', 'population': '20 mln', 'price': 'avr'}
# apt_2 = {'location': 'The Bronx', 'population': '14 mln', 'price': 'law'}
# apt_3 = {'location': 'New York', 'population': '12 mln', 'price': 'high'}
#
# apartments = [apt_1, apt_2, apt_3]
# for apt in apartments:
#     print(apt)

# === Putting a list inside a dictionary ===

apartment = {'building': 'new','amenities': ['gym', 'pool','rooftop'],}
print("I have an apartment in a " + apartment['building'] + " building with:")
for amenity in apartment['amenities']:
    print("\t" + amenity)
















