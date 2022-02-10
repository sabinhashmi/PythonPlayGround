def max_finder():
    try:
        length=int(input('What is the length of the list? '))
        list=[]
        for i in range(length):
            number=int(input(f"What is the {i+1}th digit? "))
            list.append(number)
            

        max=0

        for i in list:
            if max<i:
                max=i
        
        print(f"The maximum number in the list is {max}")

    except ValueError:
        print('Enter a digit')

max_finder()

