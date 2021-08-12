class ClassFunction():
    
    def function_01():

        length=int(input('What is the length of the list_01? '))
        list_01=[]

        for i in range(length):
            number=int(input(f"What is the {i+1}th digit? "))
            list_01.append(number)

        return list_01
        

    def function_02(list_01):
        
        max=0

        for i in list_01:
            if max<i:
                max=i
        
        print(f"The maximum number in the list_01 is {max}")

func=ClassFunction
func.function_02(func.function_01())

