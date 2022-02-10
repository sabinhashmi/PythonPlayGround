#Basics

print('Hello World')

#Entering Custom Inputs
question = input("What is your question? ")
print('Your Question is ',question)


#Triple Quotes
print(''' Triple quotes usually represent the longer messages
that can even spam across the lines.
Thanks ''')
 
#Indexing
input="This indicates indexing"
print(input[0:7])

#Formatted Coding
name="FirstName"
lname="LastName"
job='Job'
output=f'{name}[{lname}]{job} Hunter'
print(output)


#Using .format
print('This is {} way of [{}] it'.format('another','doing'))