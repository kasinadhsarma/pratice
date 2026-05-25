class triangle:
    # here parimeter of triangle = a + b + c
    # time complexity is O(1) - constant time complexity
    # space complexity is O(1) - constant space complexity
    
    def __init__(self, a , b , c):
        self.a = a
        self.b = b
        self.c = c
    def get_parimeter(self):
        return self.a + self.b + self.c


a = int(input("enter the first side of the triangle: "))
b = int(input("enter the second side of the triangle: "))
c = int(input("enter the third side of the triangle: "))
triangle = triangle(a,b,c)
print("the parimeter of the triangle is: ",triangle.get_parimeter())