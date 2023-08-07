result = int(input())
if result == 2:
    print("da")
elif result == 1: 
    print("da")
else:
    for i in range(2,result):
        if result % i == 0:
            print("No")
            break
        elif result % result == 0:
            print("Da")
            break