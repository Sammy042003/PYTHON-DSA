# Use of break, continue and pass keywords in Python

for i in range(20):
    if i == 14:
        break  # terminating the loop completely when i is 14
    if i % 2 == 0:
        continue  # skipping the rest of the loop for even numbers
    if i == 9:
        pass  # does nothing

    print(i)
    