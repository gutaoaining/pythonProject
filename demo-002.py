# 作者：顾涛
# 创建时间：2025/1/26
age = int(input("请输入你的年龄：\n"))
if age >= 60:
    print("你是老年人！你的年龄是：", age)
elif age >= 40:
    print("你是中年人！你的年龄是：", age)
elif age >= 30:
    print("你是青年人！你的年龄是：", age)
elif age >= 18:
    print("你是青少年！你的年龄是：", age)
elif age >= 12:
    print("你是少年！你的年龄是：", age)
elif age > 0:
    print("你是儿童！你的年龄是：", age)
else:
    print("你输入的年龄非法！请确认输入年龄")
