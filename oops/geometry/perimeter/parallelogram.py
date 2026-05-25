class parllelogram:
    # parimeter of parllelogram = 2 * ( a + b)
    # time complexity is O(1) - constant time complexity
    # space complexity is O(1) - constant space complexity
    
    def __init__(self, a , b):
        self.a = a
        self.b = b
    def get_parimeter(self):
        return 2 * (self.a + self.b)


a = int(input("enter the first side of the parllelogram: "))
b = int(input("enter the second side of the parllelogram: "))
parllelogram = parllelogram(a,b)
print("the parimeter of the parllelogram is: ",parllelogram.get_parimeter())