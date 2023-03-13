class empl:
    id = 160148
    name = 'Rana'
    def display(self):
        print(self.id)
emp = empl()
emp.display()

# delete object
'''class Employee():    
    id = 10   
    name = "Devansh"    
    def display (self):    
        return self.name , self.id    
        
ob1 = Employee()
del ob1.id
#print(ob1.display())'''

# Count object of class

class mp:
    count = 0
    def __init__(self):
      mp.count = mp.count + 1
s1 = mp()
s2 = mp()
s3 = mp()
print(mp.count)

# Creating parameterized constructor in python
class employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name 
    def display(self):
        return self.name, self.id

id = int(input())
name = str(input())

em1 = employee(id, name)
em2 = employee(id, name)
em3 = employee(id, name)


print(em1.display())
print(em2.display())
print(em3.display())



# Creating nonparameterized constructor in python

class employee:
    def __init__(self) :
        print('Creating nonparameterized constructor in python')
    def display(self,name):
        print(self.name)
st = employee()
st.display('Shahadat')
        
      