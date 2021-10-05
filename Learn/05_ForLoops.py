#For Loops

Prices = [10,25,67]
sum=0
for i in Prices:
    sum=sum+i
    
print(sum)


list=[5,2,5,2,2]
for i in list:
    output = ''
    for j in range(i):
        output += '*'
    print(output)