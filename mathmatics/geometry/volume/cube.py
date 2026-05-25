class cube:
    # volume of cube is s^3
    # time complexity is O(1) - constant time complexity
    # space complexity is O(1) - constant space complexity
    
    def __init__(self, s):
        self.s = s
    def get_volume(self):
        return self.s * self.s * self.s


s = int(input("enter the side of the cube: "))
cube = cube(s)
print("the volume of the cube is: ",cube.get_volume())