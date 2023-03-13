class area:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def traingle_area(self):
        return .5*self.x*self.y
    def retraingle_area(self):
        return self.x * self.y
    def circle_area(self):
        return 3.1416*self.x
    def swap_num(self):
        self.x = self.y 
        self.y =self.x
        return self.x , self.y
a = int(input())
b = int(input())

ob1 = area(a, b)
print(ob1.traingle_area())
print(ob1.retraingle_area())
print(ob1.circle_area())

print(ob1.swap_num())


        