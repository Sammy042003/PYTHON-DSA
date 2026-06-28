list_names = ["Sam", "Ruth", "John", "Duke"]

# 1st way to do it
# new_names = []
# for name in list_names:
#     name =  name + " Smith"
#     new_names.append(name)
#     print(new_names)

# 2nd way to do it
new_names =  [name + ' Smith' for name in list_names]
print(new_names)
         