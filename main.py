result = int(input())
y = 0
if result == 2:
    print("da")
elif result == 1: 
    print("da")
else:
    for i in range(2, int(result**0.5)+1):
        if result % i == 0:
            print("No")
            break
        else:
            print("Da")
            break