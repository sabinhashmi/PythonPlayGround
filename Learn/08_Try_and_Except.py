#Handling Errors (Exceptions)
#Error Code 0 represents success, anything else is a crash.

try:
    age=int(input('Enter Age '))
    print(f'Your age is {age}')
except ValueError: #In case if the user enter a string as age.
    print('Invalid Age')