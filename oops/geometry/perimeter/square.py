class square:
    # forumula of parimeter of square is 4s
    # time complexity is O(1) - constant time complexity
    # space complexity is O(1) - constant space complexity
    
    def __init__(self,s):
        self.s = s
    def get_parimeter(self):
        return 4*self.s


s = int(input("enter the side of the square: "))
square = square(s)
print("the parimeter of the square is: ",square.get_parimeter())