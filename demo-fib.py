# 作者：顾涛
# 创建时间：2025/2/2
def func(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return func(n - 1) + func(n - 2)


print(func(6))
for item in range(1, 11):
    print(func(item), end=" ")
