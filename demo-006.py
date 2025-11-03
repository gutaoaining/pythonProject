# 作者：顾涛
# 创建时间：2025/1/27
range1 = range(10)
print(list(range1))
range2 = range(101)
print(list(range2))
for item in range1:
    if item % 2 == 1:
        print("奇数：", item, end='\t')
print()
for item in range1:
    if item % 2 == 0:
        continue
    else:
        print("奇数：", item, end='\t')
print()
sumresult1 = 0
for item in range2:
    if item%2 == 0:
        print("偶数：", item, end='\t')
        sumresult1 += item
print("100以内的偶数求和是：", sumresult1)

print('-------------------求1000以内的水仙花数---------------------')
range3 = range(100, 1001, 1)
for num in range3:
    num1 = num // 100
    num2 = num // 10 % 10
    num3 = num % 10
    if num == num1**3 + num2**3 + num3**3:
        print("水仙数为：", num, num1, num2, num3)

