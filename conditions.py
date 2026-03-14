age = 25
citizen = True
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

if citizen and age >= 18:
    print("You are eligible to vote.")

temperature = 18
if temperature > 25:
    print("It's a hot day.")
elif temperature > 15:
    print("It's a warm day.")
else:
    print("It's a cold day.")


status = "Adult" if age >= 18 else "Minor"
print(status)

numbers = [1, 2, 3, 4, 4, 5]

if len(numbers) != len(set(numbers)):
    print("There are duplicate numbers in the list.")


# Matching a value against multiple cases

status = 404

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown status")

