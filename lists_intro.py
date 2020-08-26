

cars = ['BMW', 'Mercedes', 'Lexus']
print(f"I drive {cars[2]} and I like it.")
print("I drive " + cars[2] + "and I like it.")

cars[0] = 'tesla'
print(f"after: {cars}")

cars.append('BMW')
cars.insert(2, 'toyota')
print(f"after 'modification': {cars}")

del cars[2]
print(cars)

cars.remove('tesla')
print(cars)

cars.pop()
print(cars)

cars.append('BMW')
print(cars)

guests = ['Family', 'Friends', 'Coworkers']
print(f"I invite guests  but {guests[1]} could not make it.")
guests[1] = 'classmates'
print(guests)

sorted_guests = sorted(guests)
print(sorted_guests)
print(guests)

guests.sort()
print(guests)
guests.reverse()
print(guests)


nums = [2, 35, 8, 21, 7]
nums.pop(3)
print(nums)

nums = [2, 35, 8, 21, 7]
nums.remove(7)
print(nums)
print(len(nums))

# class











