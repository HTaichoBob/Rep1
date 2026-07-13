list = [64, 25, 12, 22, 11]
print("orignal list", list)
x = len(list)

for i in range(x):
    print(f"Pass {i + 1}: {list}")
    for k in range(0, x - i -1):
        if list[k] > list[k + 1]:
            list[k], list[k + 1], list[k]