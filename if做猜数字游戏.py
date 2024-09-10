import random
num = random.randint(1,120)
guess = int(input("请输入你猜测的数字:"))

if guess == num:
    print("厉害，第一次就猜中了")
elif guess > num:
    print("你猜测的大了")
else:
    print("你猜测的小了")

