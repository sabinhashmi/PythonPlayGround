#Constructer (Initialisation)
class Point:
    def __init__(self,x,y): #Initialising Co-ordinates for point
        self.x=x
        self.y=y
    
variable=Point(10,50)
print(variable.x) #Intialised value using consturctor
print(variable.y)
variable.x=25 #Re-assigning the value for co-ordinate
print(variable.x)