class Student():
    sum = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__class__.sum += 1

        print('当前班级人数:'+ str(self.__class__.sum))

    def do_homework(self):
        print('dohomework')

student1 = Student('zhujiajun',18)
student2 = Student('zjj',18)
student3 = Student('zjjj',18)