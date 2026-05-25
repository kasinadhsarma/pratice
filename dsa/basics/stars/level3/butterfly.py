class Butterfly:
    """
    Pattern (n=5):
    *        *
    **      **
    ***    ***
    ****  ****
    **********
    ****  ****
    ***    ***
    **      **
    *        *

    Upper half : left stars, gap, right stars
    Middle row : full 2n stars
    Lower half : mirror of upper
    Time Complexity  : O(N²)
    Space Complexity : O(1)
    """

    def __init__(self, n: int):
        self.n = n

    def _row(self, i: int) -> str:
        stars = "*" * i
        gap   = " " * (2 * (self.n - i))
        return stars + gap + stars

    def print_pattern(self):
        # Upper half
        for i in range(1, self.n + 1):
            print(self._row(i))
        # Lower half (mirror)
        for i in range(self.n - 1, 0, -1):
            print(self._row(i))


n = int(input("Enter number of rows (half-butterfly): "))
Butterfly(n).print_pattern()
