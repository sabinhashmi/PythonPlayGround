#Classes

class Class_01:
    def function_01(x):
        print(f'The Value of function is {x}')
        print('This is Function 01')

    def function_02():
        print('This is Function 02')


variable=Class_01

variable.function_01(20)
variable.function_02()

variable.additional_parameter=150
#To assign a value to the class
print(f'Additional Parameter is {variable.additional_parameter}') 