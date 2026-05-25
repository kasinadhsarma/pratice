class MiddleTriangle:
    """
    Pattern (n=5):
        1
       1 2
      1 2 3
     1 2 3 4
    1 2 3 4 5

    Centre-aligned: leading spaces = (n - i), numbers = 1..i.
    Time Complexity  : O(N²)
    Space Complexity : O(1)
    """

    def __init__(self, n: int):
        self.n = n

    def print_pattern(self):
        for i in range(1, self.n + 1):
            pad  = " " * (self.n - i)
            nums = " ".join(str(j) for j in range(1, i + 1))
            print(pad + nums)


n = int(input("Enter number of rows: "))
MiddleTriangle(n).print_pattern()
