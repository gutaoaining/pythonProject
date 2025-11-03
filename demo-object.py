# 作者：顾涛
# 创建时间：2025/2/6
class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.__address = address

    def show(self):
        print('展示学生：{0}的信息：,年龄：{1} ,地址：{2}'.format(self.name, self.age, self.__address))


student1 = Student('顾涛', 30, '深圳市宝安区新安街道')
student1.show()
print(student1.name)
print(student1.age)
# print(student1.__address)
# print(dir(student1))
print(student1._Student__address)
