# 作者：顾涛
# 创建时间：2025/2/1
str = 'hello,world.python'
print("index查找ll的位置：", str.index('llo'))
print("index查找o的位置：", str.index('o'))  # 返回第一个命中的位置
print('rindex查找o的位置：', str.rindex('o'))
# print('index检查不存在的字符k：', str.index('k'))
# print('rindex检查不存在的字符k：', str.rindex('k'))#不存在会报错
print('------------------------find---------------------------')
print("find查找o的位置：", str.index('o'))  # 返回第一个命中的位置
print('rfind查找o的位置：', str.rindex('o'))
print('find检查不存在的字符k：', str.find('k'))  # 不存在不会报错
print('rfind检查不存在的字符k：', str.rfind('k'))  # 不存在不会报错
print('--------------------upper、lower----------------------------')
str1 = 'helo，pyThon,wOrld'
str2 = str1.upper();
print('转换前：', str1, 'id是：', id(str1))
print('转换后：', str2, 'id是：', id(str2))
str3 = str1.lower()
print('转换前：', str1, 'id是：', id(str1))
print('转换后：', str3, 'id是：', id(str3))
str4 = str1.swapcase()
print('转换前：', str1, 'id是：', id(str1))
print('转换后：', str4, 'id是：', id(str4))
str5 = str1.capitalize()
print('转换前：', str1, 'id是：', id(str1))
print('转换后：', str5, 'id是：', id(str5))
str6 = 'helloworldtest'
str7 = str6.title()
print('转换前：', str6, 'id是：', id(str6))
print('转换后：', str7, 'id是：', id(str7))

print('-----------------------center、ljust、rjust、zzfill---------------------------')
strTemp = 'helloworld'
print(strTemp.center(20))  # 居中，不足的地方默认补空格
print(strTemp.center(20, '*'))
print(strTemp.ljust(20))  # 左对齐，不足的地方默认补空格
print(strTemp.ljust(5))  # 左对齐，不足的地方默认补空格,如果长度小于原有子字符长度，返回原有字符串

print(strTemp.ljust(20, '*'))
print(strTemp.rjust(20))  # 右对齐，不足的位置默认补空格
print(strTemp.rjust(20, '*'))
print(strTemp.zfill(20))  # 右对齐，不足的位置补0
print('-----------------------split,rsplit---------------------------')
strTemp1 = 'hello world python'
strTemp2 = 'hello,world,python'
print(strTemp1.split())
print(strTemp2.split())
print(strTemp1.rsplit())
print(strTemp2.rsplit())
print(strTemp2.split(sep=','))
print(strTemp2.split(sep=',', maxsplit=1))
print(strTemp1.split(sep=' ', maxsplit=1))
print(strTemp1.rsplit(sep=' ', maxsplit=1))
print('-----------------------------identifier,space,salpha-----------------------------------')
strTemp3 = 'adabsab_32434'
strTemp4 = 'adabsab_32434_$_&'
print(strTemp3, "是否是合法标识符组成：", strTemp3.isidentifier())
print(strTemp4, "是否是合法标识符组成：", strTemp4.isidentifier())
print('''\t''', '是空制表符：', '\t'.isspace())
print('''''', '是空制表符：', ''.isspace())
print(''' ''', '是空制表符：', ' '.isspace())
print(strTemp3, "是否是字母组成：", strTemp3.isalpha())
print(strTemp4, "是否是字母组成：", strTemp4.isalpha())
print('asdasdererfdg', "是否是字母组成：", 'asdasdererfdg'.isalpha())
print(strTemp3, "是否是字母和数字组成：", strTemp3.isalnum())
print(strTemp4, "是否是字母和数字组成：", strTemp4.isalnum())
print('asd343134三', "是否是字母和数字组成：", 'asd343134三'.isalnum())
print('343134三', "是否是字母和数字组成：", '343134三'.isalnum())
print('23412341三', "是否是十进制数字组成：", '23412341三'.isdecimal())
print('23412341', "是否是十进制数字组成：", '23412341'.isdecimal())
print('23412341三', "是否是数字组成：", '23412341三'.isnumeric())
print('23412341', "是否是数字组成：", '23412341'.isnumeric())
print('a23412341', "是否是数字组成：", 'a23412341'.isnumeric())
print('--------------------------replace join------------------------------')
strTest1 = 'hello,python,python,world'
print(strTest1.replace('python', 'java', 1))
print(strTest1.replace('python', 'java', 2))
print(strTest1)
list1 = ['hello', 'python', 'world']
print(''.join(list1))
print(' '.join(list1))
print(','.join(list1))
print(list1)
print(','.join('list1'))
list2 = ('hello', 'python', 'world')
print(' '.join(list2))

print('apple' > 'app')
print('apple' > 'bag')
print('a的编码：', ord('a'), 'b的编码：', ord('b'))
print('97的编码对应字符：', chr(97), '98的编码对应字符：', chr(98))
test1 = 'application'
test2 = 'application'
print(test1 is test2)
print(test1 >= test2)
test3 = 'hello java world'
print(test3[1:5:1])
print(test3[::2])
print(test3[::-2])
print(test3[-6::-2])
print('-------------------------str format------------------------')
name = '顾涛'
age = 30
print("我是%s，今年%d岁" % (name, age))
print("我是{0}，今年{1}岁".format(name, age))
print(f"我是{name}，今年{age}岁")
print('%10d' % 10)
print('helloworld')
print('%10d' % 10)
print('%10.3f' % 3.1415926)
print('{0:10.3f}'.format(3.1415926))
print('----------------------------encode decode--------------------------------')
test5 = '待到秋来九月八'
print(test5.encode(encoding='GBK'))#一个汉字两个字节
print(test5.encode(encoding='UTF-8'))#一个汉字三个字节
b_g= test5.encode(encoding='GBK')
print(b_g.decode(encoding='GBK'))
b_u = test5.encode(encoding='UTF-8')
print(b_u.decode(encoding='UTF-8'))


