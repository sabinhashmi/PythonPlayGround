#While Loops

i = 1
while i <= 10: #As long as this statement is true, it will keep iterating.
    print('*' * i)
    i = i + 1 #if this statement is not there, it will be an endless loop
print('Complete Iteration ')


#Guessing number
number=9
guess_try=0
max_guess=3
while guess_try<max_guess:
    num=int(input('Guess the number ? '))
    guess_try += 1
    if num==number:
        print('You Win')
        break
    else:
        print('Try again.!')
else: #While Loop has a else block option
    print('Maximum Number of Tries Exhausted !')