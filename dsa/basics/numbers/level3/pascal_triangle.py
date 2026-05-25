class PascalTriangle:
    """
    Pattern (n=5):
            1
          1   1
        1   2   1
      1   3   3   1
    1   4   6   4   1

    Pascal's rule: C(i, j) = C(i-1, j-1) + C(i-1, j)
    Each element is a binomial coefficient C(row, col).

    Time Complexity  : O(N²)
    Space Complexity : O(N)  — one row stored at a time
    """

    def __init__(self, n: int):
        self.n = n

    def _binomial(self, row: int, col: int) -> int:
        """C(row, col) computed iteratively."""
        if col == 0 or col == row:
            return 1
        col = min(col, row - col)   # use symmetry
        result = 1
        for i in range(col):
            result = result * (row - i) // (i + 1)
        return result

    def print_pattern(self):
        width = len(str(self._binomial(self.n - 1, (self.n - 1) // 2)))
        for i in range(self.n):
            pad  = " " * ((self.n - i - 1) * (width + 1))
            nums = ("   ").join(
                str(self._binomial(i, j)).center(width)
                for j in range(i + 1)
            )
            print(pad + nums)


n = int(input("Enter number of rows: "))
PascalTriangle(n).print_pattern()
