#面向对象编程是一种程序设计思想，一个对象包含了数据和操作数据的函数
class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def  print_score(self):
        print("%s : %s"%(self.__name,self.__score))

bart = Student("jack",20)
bart.print_score()
bart.__name = "james"
bart.print_score()
print(dir("123"))
#getattr hasattr setattr