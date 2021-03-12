# fruit = {"Orange": "a sweet, orange citrus fruit",
#          "lemon": "a sour, yellow citrus fruit",
#          "grape": "a small sweet fruit, grown in bunches",
#          "lime": "a sour, green citrus fruit",
#          "apple": "good for making cider",
#          }
# print(fruit["apple"])
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
# fruit["pear"] = "great with tequila"
# print(fruit)
#
# del fruit["lemon"]
# print(fruit)
#
# # to clear a dictionary
# fruit.clear()

# to prevent an error when a key is not in a dictionary
fruit = {"orange": "a sweet, orange citrus fruit",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small sweet fruit, grown in bunches",
         "lime": "a sour, green citrus fruit",
         "apple": "good for making cider",
         }
# while True:
#     fruit_input = input("Enter a fruit: ")
#     if fruit_input == "quit":
#         break
#     if fruit_input in fruit:
#         description = fruit.get(fruit_input)
#         print(description)
#     else:
#         print("Not Available!")
# the above code is also the same as
#     description = fruit.get(fruit_input, "Not Available!")
# providing a default value to the get method

for i in fruit:
    print("{} is {}".format(i, fruit[i]))
print("*" * 50)

# fruit.keys() returns a list, but not the list we are used to
# ordering a dictionary
ordered_keys = list(fruit.keys())
ordered_keys.sort()
for i in ordered_keys:
    print("{} -- {}".format(i, fruit[i]))

print("*" * 50)
for val in fruit.values():
    print(val)
print()
for keys in fruit.keys():
    print(keys)

print("*" * 50)

print(fruit.values())
print(fruit.keys())
print(list(fruit))
print(fruit.items())

# creating a tuple with fruit.items()
f_tuple = tuple(fruit.items())
print(f_tuple)
