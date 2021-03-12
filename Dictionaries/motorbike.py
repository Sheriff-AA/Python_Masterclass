bike = {"make": "Honda", "model": "250 Dream", "colour": "Red", "engine_size": 250}

print(bike["engine_size"])

user_prompt = input("Enter a bike spec: ").casefold()

words = user_prompt.split()

for word in words:
    if word in bike:
        print(bike[word])
        break
else:
    print("Spec. not Available!")
