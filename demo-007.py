# 作者：顾涛
# 创建时间：2025/1/27
range1 = range(5)
for num1 in range1:
    print(num1, end="\t")

passwordNum = range(3)
for num in passwordNum:
    password = input("请输入你的密码：")
    if password == '8888':
        print("密码输入正确！")
        break
    else:
        print("密码输入错误，请重新输入！")
else:
    print("密码输入错误次数超过3次，不能再输入！")

a = 0
while a < 3:
    password = input("请输入密码：")
    if password == '8888':
        print('密码输入正确！')
        break;
    else:
        print('密码输入错误！请重新输入！')
        a += 1
else:
    print("输入密码错误次数超过3次！结束输入！")