__all__ = ["g_num", "show"]
# 指定 all 表示 from 模块名 import * 只能使用指定的功能代码，而不是所有的功能代码

# 定义全局变量
g_num = 10

# 定义函数
def show():
    print("我是一个函数")

# 定义类
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_msg(self):
        print(self.name, self.age)

# 解决导入的模块中方法没有调用就执行
if __name__ == "__main__":
    show()