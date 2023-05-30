import random
start = input("請輸入最小範圍")
end = input("請輸入最大範圍")
r = random.randint(int(start), int(end))
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