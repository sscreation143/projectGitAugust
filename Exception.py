# num1=int(input('enter the number'))
# num2=int(input('enter the number 2'))

# div=None
# try:
#     div=num1/num2
#     print('try runs')
# except:
#     print('exection ocuured')
# print('continue execution')
# if div!=None:
#     print('result:',div)

import traceback,sys
#Types of error
#1. Compile time error
#2. Logical error(Deviation in output)-Corrected by debugging technique
#3. Runtime error(Serious error occurs during execution time).
'''print(BaseException.mro())#is an exception class for all runtime errors
print(Exception.mro())
print(ZeroDivisionError.mro())
print(IndexError.mro())
print(SyntaxError.mro())'''
def func():
    print('fuction running')
#num1=int(input('Enter a number'))
#num2=int(input('Enter another number'))
div=None
a=[12,45,65]
try:
    num1=int(input('Enter a number'))
    num2=int(input('Enter another number'))
    #print(a[5])
    div=num1/num2
    print('Try runs ')
#except:
#except(BaseException)as e:
#except(Exception)as e:
#except(ArithmeticError)as e:
except(ZeroDivisionError,ValueError)as e:
    traceback.print_exc(file=sys.stdout)
    print('Exception occured')
    func()
else:
    print('Result:',div)
finally:
    print('finally executes')
'''except(ZeroDivisionError)as e:
    traceback.print_exc(file=sys.stdout)
    print('Exception occured')
except(ValueError)as e:
    print(e)
    traceback.print_exc(file=sys.stdout)
    print('Exception occured')'''
print('Main continues')
'''if div:
    print('Result:',div)'''


class AgeException(Exception):
    def __init__(self, msg):
        super().__init__(msg)  # Exception class

class Employee:
    def __init__(self, name, age):
        if age < 18 :
            raise AgeException('Age cannot be less than 18 years')  # create own excetions using inheritance
        else:
            self.age = age
        self.name = name

try:
    ob = Employee('Sathish', 22)
                # raise AgeException('Age cannot be less than 18 years')
                # __main__.AgeException: Age cannot be less than 18 years
except(AgeException) as e:
    print('Exception Age Handled')
print('Main Continues')
