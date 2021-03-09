for i in range(1, 11):
    for j in range(1, 13):
        print(i, i * j)


for num, multiply in [(i, i * j) for i in range(1, 11) for j in range(1, 13)]:
    print(num, multiply)

times = [(i, i * j) for i in range(1, 11) for j in range(1, 13)]
print(times)
