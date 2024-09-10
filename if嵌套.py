print("获取考试资格")
print("获取条件(智商超过100或者家庭资产超过1000000)")
Iq = int(input("请输入你的智商："))
if Iq >= 100:
    print("智商超过100，你以获取考试资格！")
else:
    HAssert = int(input("请输入你的家庭资产："))
    if HAssert >= 1000000:
        print("家庭资产达到100w以上，你已获得考试资格！")
    else:
        print("你个又蠢又没钱的傻逼，不配进来考试！")

