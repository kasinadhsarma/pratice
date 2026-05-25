class Diamond:
    """
    Pattern (n=5):
        *
       ***
      *****
     *******
    *********
     *******
      *****
       ***
        *

    Upper half  : pyramid (rows 1..n)
    Lower half  : inverted pyramid (rows n-1..1)
    Time Complexity  : O(N²)
    Space Complexity : O(1)
    """

    def __init__(self, n: int):
        self.n = n

    def print_pattern(self):
        # Upper half (including middle)
        for i in range(1, self.n + 1):
            print(" " * (self.n - i) + "*" * (2 * i - 1))
        # Lower half
        for i in range(self.n - 1, 0, -1):
            print(" " * (self.n - i) + "*" * (2 * i - 1))


n = int(input("Enter number of rows (half-diamond): "))
Diamond(n).print_pattern()
