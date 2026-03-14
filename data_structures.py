# LISTS

numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed = [1, "Hello", 3.14, True]

# Accessing list elements
print(numbers[0])  # Output: 1
print(names[1])    # Output: Bob
print(mixed[2])    # Output: 3.14

# Modifying list elements
numbers[0] = 10
print(numbers)  # Output: [10, 2, 3, 4, 5]
# Adding elements to a list
numbers.append(6)
print(numbers)  # Output: [10, 2, 3, 4, 5, 6]
# Removing elements from a list
numbers.remove(2)
print(numbers)  # Output: [10, 3, 4, 5, 6]
# inserting elements at a specific position
numbers.insert(1, 20)
print(numbers)  # Output: [10, 20, 3, 4, 5, 6]

# Iterating through a list
for number in numbers:
    print(number)


# Practice tasks:
# 1. Create a list of your favorite fruits and print it.
fruits = ["Apple", "Banana", "Cherry"]
print(fruits[0])
fruits.append("Orange")
print(fruits)
fruits.remove("Banana")
print(fruits)
print(len(fruits))

# TUPLES

coordinates = (10, 20)

def get_user():
    return ("Alice", 30)

name, age = get_user()
print(name)
print(age)


# SETS

nums = {1, 2, 3, 4, 4, 5}
print(nums)  # Output: {1, 2, 3, 4, 5}

nums.add(6)
print(nums)  # Output: {1, 2, 3, 4, 5, 6}

set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a.union(set_b))  # Output: {1, 2, 3, 4, 5}
print(set_a.intersection(set_b))  # Output: {3}
print(set_a.difference(set_b))  # Output: {1, 2}

# DICTIONARIES

user = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(user["name"])  # Output: Alice
print(user["age"])   # Output: 30
print(user["city"])  # Output: New York

user["age"] = 31
print(user)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}

user["email"] = "alice@example.com"
print(user)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'email': 'alice@example.com'}

del user["city"]
print(user)  # Output: {'name': 'Alice', 'age': 31, 'email': 'alice@example.com'}

for key, value in user.items():
    print(f"{key}: {value}")

car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2020
}
print(car["model"])  # Output: Camry

nums = [1, 2, 3, 4, 4, 5]
print(set(nums))  # Output: {1, 2, 3, 4, 5}