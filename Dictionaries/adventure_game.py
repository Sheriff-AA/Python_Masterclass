new_location = {
    0: {"desc": "Loading Screen",
        "exits": {},
        "namedExits": {},
        },
    1: {"desc": "On a Road",
        "exits": {"Q": 0, "W": 2, "S": 4, "N": 5, "E": 3},
        "namedExits": {"2": 2, "4": 4, "5": 5, "3": 3},
        },
    2: {"desc": "Top of a Hill",
        "exits": {"N": 5, "Q": 0},
        "namedExits": {"5": 5},
        },
    3: {"desc": "In a building",
        "exits": {"W": 1, "Q": 0},
        "namedExits": {"1": 1},
        },
    4: {"desc": "In a valley",
        "exits": {"N": 1, "W": 2, "Q": 0},
        "namedExits": {"1": 1, "2": 2},
        },
    5: {"desc": "A forest",
        "exits": {"W": 2, "S": 1, "Q": 0},
        "namedExits": {"2": 2, "1": 1},
        },
}

# locations = {0: "Loading Screen",
#              1: "On a road",
#              2: "Top of a hill",
#              3: "In a building",
#              4: "In a valley",
#              5: "A forest",
#              }
#
# exits = {
#     0: {"Q": 0},
#     1: {"Q": 0, "W": 2, "S": 4, "N": 5, "E": 3},
#     2: {"N": 5, "Q": 0},
#     3: {"W": 1, "Q": 0},
#     4: {"N": 1, "W": 2, "Q": 0},
#     5: {"W": 2, "S": 1, "Q": 0},
# }
#
# named_Exits = {
#     1: {"2": 2, "4": 4, "5": 5, "3": 3},
#     2: {"5": 5},
#     3: {"1": 1},
#     4: {"1": 1, "2": 2},
#     5: {"2": 2, "1": 1},
# }

alternate_words = {"quit": "Q",
                   "north": "N",
                   "up": "N",
                   "south": "S",
                   "down": "S",
                   "west": "W",
                   "left": "W",
                   "east": "E",
                   "right": "E",
                   "road": "1",
                   "hill": "2",
                   "building": "3",
                   "valley": "4",
                   "forest": "5",
                   }

loc = 1
while True:
    available_exits = ", ".join(new_location[loc]["exits"].keys())

    print(new_location[loc]["desc"])

    if loc == 0:
        break
    else:
        allExits = new_location[loc]["exits"].copy()
        allExits.update(new_location[loc]["namedExits"])

    direction = input("Available exits are {} "
                      .format(available_exits)).casefold()
    print()
    # parse the user input using alternate_words if necessary
    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in alternate_words:
                direction = alternate_words[word]
                break
        # for word in alternate_words:    # does it contain a word we know?
        #     if word in direction:
        #         direction = alternate_words[word]

    if direction in allExits:
        loc = allExits[direction]
    else:
        print("Dead end")

# dictionaries have the advantage that insertion and deletion are very fast
# access by key is also fast
