class InvertedPyramid:
    """
    Pattern (n=5):
    *********
     *******
      *****
       ***
        *

    Time Complexity  : O(N²)
    Space Complexity : O(1)
    """

    def __init__(self, n: int):
        self.n = n

    def print_pattern(self):
        for i in range(self.n, 0, -1):
            spaces = " " * (self.n - i)
            stars  = "*" * (2 * i - 1)
            print(spaces + stars)


n = int(input("Enter number of rows: "))
InvertedPyramid(n).print_pattern()
