class rectanglularprism:
    # volume of rectanglularprism is l * w * h
    # time complexity is O(1) - constant time complexity
    # space complexity is O(1) - constant space complexity
    
    def __init__(self, l , w , h):
        self.l = l
        self.w = w
        self.h = h
    def get_volume(self):
        return self.l * self.w * self.h


l = int(input("enter the length of the rectanglularprism: "))
w = int(input("enter the width of the rectanglularprism: "))
h = int(input("enter the height of the rectanglularprism: "))
rectanglularprism = rectanglularprism(l,w,h)
print("the volume of the rectanglularprism is: ",rectanglularprism.get_volume())