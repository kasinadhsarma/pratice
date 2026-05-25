class trapezoid:
    # parimeter of trapezoid  = a   + b1 + b2 + c
    # time complexity is O(1) - constant time complexity
    # space complexity is O(1) - constant space complexity
    
    def __init__(self, a , b1 , b2 , c):
        self.a = a
        self.b1 = b1
        self.b2 = b2
        self.c = c
    def get_parimeter(self):
        return self.a + self.b1 + self.b2 + self.c


a = int(input("enter the first side of the trapezoid: "))
b1 = int(input("enter the second side of the trapezoid: "))
b2 = int(input("enter the third side of the trapezoid: "))
c = int(input("enter the fourth side of the trapezoid: "))
trapezoid = trapezoid(a,b1,b2,c)
print("the parimeter of the trapezoid is: ",trapezoid.get_parimeter())