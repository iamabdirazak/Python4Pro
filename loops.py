logs = [
    "login",
    "view_page",
    "debug",
    "click_button",
    "skip",
    "logout",
    "shutdown"
]

for event in logs:

    if event == "debug":
        continue  # Skip debug events

    if event == "skip":
        pass

    elif event == "shutdown":
        print("System is shutting down...")
        break  # Stop processing logs on shutdown

    print(f"Processing event: {event}")


# While loop example

counter = 0

while counter < 5:
    print(f"Counter is at: {counter}")
    counter += 1

    word = "Python"

    for letter in word:
        print(f"Letter: {letter}")


# Loop over a dictionary

user = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

for key, value in user.items():
    print(f"{key}: {value}")


for i in range(2, 12, 2):
    print(f"Number: {i}")

for n in range(5):
    
    if n == 3:
        break
    print(n)
else:
    print("Loop finished")