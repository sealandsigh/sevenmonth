from test1 import Human

class Student(Human):
    sum = 0

    def __init__(self,school,name,age):
        self.school = school
        super(Student,self).__init__(name,age)
        #self.__class__.sum += 1

        #print('当前班级人数:'+ str(self.__class__.sum))

    def do_homework(self):
        print('dohomework')

    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)

student1 = Student('人民路小学','zhujiajun',18)
student1.get_name()