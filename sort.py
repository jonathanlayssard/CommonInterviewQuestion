number = [64, 25, 12, 22, 11, 1, 2, 44, 3, 122, 23, 34]

for i in range(len(number)):
    for j in range(i + 1, len(number)):

        if number[i] > number[j]:
            number[i], number[j] = number[j], number[i]

print(number)