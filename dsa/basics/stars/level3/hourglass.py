class Hourglass:
    """
    Pattern (n=5):
    *********
     *******
      *****
       ***
        *
       ***
      *****
     *******
    *********

    Upper half  : inverted pyramid (rows n..1)
    Lower half  : pyramid without middle (rows 2..n)
    Time Complexity  : O(N²)
    Space Complexity : O(1)
    """

    def __init__(self, n: int):
        self.n = n

    def print_pattern(self):
        # Upper half (narrowing down to tip)
        for i in range(self.n, 0, -1):
            print(" " * (self.n - i) + "*" * (2 * i - 1))
        # Lower half (expanding back up, skip tip)
        for i in range(2, self.n + 1):
            print(" " * (self.n - i) + "*" * (2 * i - 1))


n = int(input("Enter number of rows (half-hourglass): "))
Hourglass(n).print_pattern()
