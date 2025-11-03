# 作者：顾涛
# 创建时间：2025/1/27
list1 = [10, 30, 20, 50, 40, 60, 70, 80, 90]
list2 = list([10, 20, 30, 40, 50, 60, 70, 80, 90])
print(id(list1))
print(type(list1))
print(id(list2))
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
list3 = list1[1:8:1]
print(list3)
list4 = list1[8:0:-1]
print(list4)
print(10 in list1)
print(100 in list1)
print(list1.index(10))
print(list1[1])

