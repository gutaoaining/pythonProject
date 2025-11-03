# 作者：顾涛
# 创建时间：2025/1/30
scores = {'顾涛': 90, '小宁': 100, '张三': 55}
print(scores)
scores['李四'] = 77
print(scores)
del scores['李四']
print(scores)
keys = scores.keys()
print(keys)
values = scores.values()
print(values)
for item in scores:
    print(item, scores.get(item),scores.items())
listKey = ['key1', 'key2', 'key3', 'key4']
listValue = ['value1', 'value2', 'value3']
d = {key.upper(): value for key, value in zip(listKey, listValue)}
print(d)
