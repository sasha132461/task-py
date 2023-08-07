result = int(input())
y = 0
if result == 2:
    print("da")
elif result == 1: 
    print("da")
else:
    for x in range(2, result, result - 1):
        for y in range(2,x):
            if y / x == 0:
                y += 1
    for i in range(2,result):
        for j in range(2, i):
            if i % j == 0:
                y += 2
if y == 1:
    print("Da")
else:
    print("No")