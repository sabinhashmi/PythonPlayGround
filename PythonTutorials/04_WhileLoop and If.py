condition=''
while True: # or while condition.upper() != 'QUIT':
    condition=input('Enter condition ')
    if condition.upper()=='START':
        print('Car Started')
    elif condition.upper() == 'STOP':
        print('Car Stopped')
    elif condition.upper() == 'QUIT':
        print('Quit')
        break
    else:
        print('Command not Understandable')
