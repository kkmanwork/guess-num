import random
r = random.randint(1, 100)
count = 0
while True:
    num = input("請猜一個數字")
    num = int(num)
    count += 1
    if r == num:
        print("終於猜對了，妳總共猜了", count, "次" )
        break
    elif num > r:
        print("比答案大")
    elif num < r:
        print("比答案小")
    print("這是妳猜的第", count, "次")