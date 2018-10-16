class Student():
    def __init__(self,name,address):
        self.name = name
        self.address = address
    
    def greet(self,age):
        self.age = age
        print ('Hello my name is {0} and I live in {1}').format(self.name,self.address)

class Dev(Student):
    def __init__(self,name,address,_type):
        Student.__init__(self,name,address)
        self._type = _type


C1 = Student("Binayak","Kathmandu")
print (C1.greet("20"))
C2 = Dev ("John","Putalisadak","Student")
print (C2.greet('21..'))

a = [("Kathmandu",30),("Chitwan",45)]

temps = lambda data: (data[0], (9/5)* data[1] +32)

value = list(map(temps, a))

print (value)