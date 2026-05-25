class NumberButterfly:
    """
    Pattern (n=5):
    1                1
    1 2          1 2
    1 2 3      1 2 3
    1 2 3 4  1 2 3 4
    1 2 3 4 51 2 3 4 5
    1 2 3 4  1 2 3 4
    1 2 3      1 2 3
    1 2          1 2
    1                1

    Row i: nums 1..i + gap (2*(n-i) spaces) + nums 1..i  (mirrored)
    Upper half rows 1..n, lower half rows n-1..1
    Time Complexity  : O(N²)
    Space Complexity : O(1)
    """

    def __init__(self, n: int):
        self.n = n

    def _row(self, i: int) -> str:
        nums = " ".join(str(j) for j in range(1, i + 1))
        gap  = " " * (2 * (self.n - i) + 1)
        return nums + gap + nums

    def print_pattern(self):
        for i in range(1, self.n + 1):
            print(self._row(i))
        for i in range(self.n - 1, 0, -1):
            print(self._row(i))


n = int(input("Enter number of rows (half-butterfly): "))
NumberButterfly(n).print_pattern()
