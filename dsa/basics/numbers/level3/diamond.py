class NumberDiamond:
    """
    Pattern (n=5):
            1
          1 2 1
        1 2 3 2 1
      1 2 3 4 3 2 1
    1 2 3 4 5 4 3 2 1
      1 2 3 4 3 2 1
        1 2 3 2 1
          1 2 1
            1

    Upper half  : palindrome pyramid rows 1..n
    Lower half  : palindrome pyramid rows n-1..1
    Time Complexity  : O(N²)
    Space Complexity : O(1)
    """

    def __init__(self, n: int):
        self.n = n

    def _row(self, i: int) -> str:
        ascending  = list(range(1, i + 1))
        descending = list(range(i - 1, 0, -1))
        nums = ascending + descending
        pad  = " " * ((self.n - i) * 2)
        return pad + " ".join(str(x) for x in nums)

    def print_pattern(self):
        for i in range(1, self.n + 1):
            print(self._row(i))
        for i in range(self.n - 1, 0, -1):
            print(self._row(i))


n = int(input("Enter number of rows (half-diamond): "))
NumberDiamond(n).print_pattern()
