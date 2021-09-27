
    
#count=15 #Global variable
#1.Classes and objects
#2. Encapsulation(Name Mangling)
class Employee:
    count=0 #class variable
    #does not support method overloading and constructor overloading.
def __init__(self,name='',age=18,phone=''):# is a special predefined function of Python Library
                       # is a constructor declaration
    count=11 #Local variable
print('init method runs')
    self.name=name#instance variable
    self.age=age#instance variable
    self.__phone=phone #Name Mangling
print(self)
        Employee.count+=1
# globals()['count']+=1
print(count)
        print(Employee.count)
        #print(globals()['count'])
    #Method(static,non static and class Method)
def show(self):#Non static method
        #print('Name:',self.name)
        #print('Age:',self.age)
print('Count:',Employee.count)
        return self.name,self.age
    @classmethod#
def getCount(cls):
        print('Count:',cls.count)
    @staticmethod
def get():#static method
print('get is a static method')
Employee.get()
Employee.getCount()
emp1=Employee("Chandra",35,8527818630)#(super().init()-object class
Employee.getCount()
emp1.show()
#print('No. Of Objects:',Employee.count)
#print(emp1)
'''print('Employee Details:',emp1)
#Approach 2
name,age=emp1.show()
print('Name',name)
print('Age',age)
#Approach 3
print('Name',emp1.name)
print('Age',emp1.age)
emp2=Employee()
print('No. Of Objects:',Employee.count)
print(emp2)'''
#Approach 1
print('Details of emp1:',emp1.__dict__)
#print('Details of emp2:',emp2.__dict__)
print('Phone Number:',emp1._Employee__phone)
