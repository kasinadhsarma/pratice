class LeftTriangle:
    """
    Pattern (n=5):
            1
          1 2
        1 2 3
      1 2 3 4
    1 2 3 4 5

    Right-aligned: leading spaces = (n - i) * 2 so columns line up.
    Time Complexity  : O(N²)
    Space Complexity : O(1)
    """

    def __init__(self, n: int):
        self.n = n

    def print_pattern(self):
        for i in range(1, self.n + 1):
            # each number takes 2 chars, so pad (n-i) * 2 spaces
            spaces = " " * ((self.n - i) * 2)
            nums   = " ".join(str(j) for j in range(1, i + 1))
            print(spaces + nums)


n = int(input("Enter number of rows: "))
LeftTriangle(n).print_pattern()
