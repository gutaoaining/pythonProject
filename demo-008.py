# 作者：顾涛
# 创建时间：2025/1/27
for i in range(1, 10):
    for j in range(1, 10):
        print("*", end="\t")
    print()
for i in range(1, 10):
    for j in range(1, i+1):
        print(i ,"*", j, '=', i * j, end="\t")
    print()