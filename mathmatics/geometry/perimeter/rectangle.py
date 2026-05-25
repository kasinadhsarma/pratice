class square:
    # forumula of parimeter of rectangle is 2 * ( l + w)
    # here time complexity is O(1) - constant time complexity
    # here space complexity is O(1) - constant space complexity
    
    def __init__(self, l , w):
        self.l = l
        self.w = w
    def get_parimeter(self):
        return 2 * (self.l + self.w)


l = int(input("enter the length of the rectangle: "))
w = int(input("enter the width of the rectangle: "))
rectangle = square(l,w)
print("the parimeter of the rectangle is: ",rectangle.get_parimeter())