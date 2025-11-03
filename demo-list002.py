# 作者：顾涛
# 创建时间：2025/1/27
list1 = [20, 80, 10]
list2 = ['hello', 'world']
list3 = list(['test', 'python', 90, 80])
print(id(list1), "list1添加元素之前：", list1)
list1.append(100)
print(id(list1), "list1添加元素之后：", list1)
print(id(list2), "list2添加元素之前：", list2)
list2.insert(1, '测试')
print(id(list2), "list2添加元素之后：", list2)
list1.extend(list2)
print(id(list1), list1)
list1.remove('测试')
print(id(list1), list1)
list1.pop(0)
print(id(list1), list1)
list1.pop()
print(id(list1), list1)
new_list = list1[1:3]
print(new_list)
print(id(list1), list1)
list1[1:3] = []
print(id(list1), list1)
list1[1] = 'world'
print(id(list1), list1)
list1.append(100)
list1.append(300)
print(id(list1), list1)
list1[1:3] = [2, 3, 4, 5, 6, 7]
sort_list = sorted(list1)
print(id(list1), list1)
print(id(list1), "list1源对象：", list1)
print(id(sort_list), "list排序之后：", sort_list)
list3.append(list2)
print(list3)
list1.clear()
print(list1)

list5 = [i * i for i in range(1, 10)]
print(list5)
# del list1
# print(list1)
