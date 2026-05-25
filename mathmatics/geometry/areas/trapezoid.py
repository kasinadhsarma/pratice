class trapezoid:
    # here formula of area of trapezoid is h (b1+b2)/2
    # here time complexity is O(1) - constant time complexity
    # here space complexity is O(1) - constant space complexity
    
    def __init__(self, h , b1 , b2):
        self.h = h
        self.b1 = b1
        self.b2 = b2
    def get_area(self):
        return self.h * (self.b1 + self.b2) / 2


h = int(input("enter the height of the trapezoid: "))
b1 = int(input("enter the first base of the trapezoid: "))
b2 = int(input("enter the second base of the trapezoid: "))
trapezoid = trapezoid(h,b1,b2)
print("the area of the trapezoid is: ",trapezoid.get_area())