# use for for, while keywords

# defining a list
stuff = ["Mango", "Banana", "Apple", "Grapes"]
print("Given List:", stuff)

print("\nIterating Over List using 'for' loop:")
# iterating over the list using for loop
for items in stuff:
    print(items)

print("\nIterating Over List using 'while' loop:")
# iterating over the list using while loop
index = 0
while index < len(stuff):
    print(stuff[index])
    index += 1
