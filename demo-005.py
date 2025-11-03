# 作者：顾涛
# 创建时间：2025/1/26
a = 100
a += 200
print(a)
str1 = "helloword"
str2 = "helloword"
print("str1和str2的值是否相等：", str2 == str1)
print("str1和str2的ID是否相等：", id(str2) == id(str1))
list1 = list(['1', '2'])
list2 = list(['1', '2'])
print("list1和list2的值是否相等：", list1 == list2)
print("list1和list2的id是否相等：", id(list1) == id(list2))
print(list1 is not list2)
print(str2 is not str1)
print(10 // 2)
print(9 % 2)
print(-9 // 2)
print(9 // -2)
print(-9 % 2) #取余一整一负的时候等于被除数 - 除数 * 商，-9 - （2* -5）= -9+10 = 1
print(9 % -2) #取余一整一负的时候等于被除数 - 除数 * 商，9 - （-2* -5）= 9 -10 = -1



