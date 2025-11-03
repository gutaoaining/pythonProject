# 作者：顾涛
# 创建时间：2025/2/2
def fuc1(n):
    if n == 1:
        return 1
    else:
        return n * fuc1(n - 1)

print(fuc1(6))
