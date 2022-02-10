#To find maximum:

numbers=[2,5,2,6,78,9,4]
max=0
for i in numbers:
    if i>max:
        max=i
print(max)


#To check for duplicates

numbers=[2,5,2,6,78,9,4]
unique=[]
for i in numbers:
    if i not in unique:
        unique.append(i)
print(unique)