# 作者：顾涛
# 创建时间：2025/1/26
print(1)
print("测试")
print(str(2))
num1 = 2
float1 = 2.1
str1 = '5'
print(num1, type(num1))
print(float1, type(float1))
print(str1, type(str1))
print('---------str转换后---------')
change1 = str(num1)
change2 = str(float1)
print(change1, type(change1))
print(change2, type(change2))
print('---------int转换后---------')
change3 = int(str1)
change4 = int(float1)
print(change3, type(change3))
print(change4, type(change4))
print('---------float转换后---------')
change5 = float(num1)
change6 = float(str1)
print(change5, type(change5))
print(change6, type(change6))