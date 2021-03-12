fruit = {"orange": "a sweet, orange citrus fruit",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small sweet fruit, grown in bunches",
         "lime": "a sour, green citrus fruit",
         "apple": "good for making cider",
         }

veggies = {"carrot": "a long sweet orange vegetable",
           "tomato": "reddish-like round fruit",
           "cabbage": "not bad",
           "spinach": "get me candy please",
           }

veggies.update(fruit)
print(veggies)

veg_and_fruit = fruit.copy()
veg_and_fruit.update(veggies)
print(veg_and_fruit)
