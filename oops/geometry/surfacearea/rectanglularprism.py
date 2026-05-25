class rectanglularprism:
    # here surface area of rectanglularprism is 2 * (lw + lh + wh)
    # time complexity is O(1) - constant time complexity
    # space complexity is O(1) - constant space complexity
    
    def __init__(self, l , w , h):
        self.l = l
        self.w = w
        self.h = h
    def get_surface_area(self):
        return 2 * (self.l * self.w + self.l * self.h + self.w * self.h)


l = int(input("enter the length of the rectanglularprism: "))
w = int(input("enter the width of the rectanglularprism: "))
h = int(input("enter the height of the rectanglularprism: "))
rectanglularprism = rectanglularprism(l,w,h)
print("the surface area of the rectanglularprism is: ",rectanglularprism.get_surface_area())