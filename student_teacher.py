#!/usr/bin/env python3
import sys
from collections import Counter
class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name
    def get_grade(self):
        return self.grade
class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, branch, year, grade):
        Person.__init__(self, name, grade)
        self.branch = branch
        self.year = year
        self.grade = grade

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)

    def get_grade(self):
        fail = 0
        Pass = 0
        for i in self.grade:
            if i == 'D':
                fail+=1
            else:
                Pass+=1
        return "Pass: {}, Fail: {}".format(Pass, fail)

class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers, grade):
        Person.__init__(self, name, grade)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

    def get_grade(self):
        a = Counter(self.grade).most_common(4)
        c = ','.join('{}: {}'.format(*i)for i in a)
        sorted(c)
        print(c)
#person1 = Person('a' ,'A')

student = Student('Kushal', 'CSE', 2005, sys.argv[2])
teacher = Teacher('Prashad', ['C', 'C++'], sys.argv[2])

#print(person1.get_details())
if sys.argv[1] == 'student':
    print(student.get_grade())
elif sys.argv[1] == 'teacher':
    teacher.get_grade()

