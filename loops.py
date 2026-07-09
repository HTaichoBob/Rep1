my_list = [5, 18, 487, 11, 2, 4, 85, 66, 448, 47, 78, 600, 8, 12, 78, 20, 4, 78, 27461, 26]
multiples_of_three = []
for number in my_list:
    if number % 3 ==0:
        multiples_of_three.append(number)

print(multiples_of_three)
