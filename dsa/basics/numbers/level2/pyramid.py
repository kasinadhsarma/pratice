class NumberPyramid:
    """
    Pattern (n=5):
            1
          1 2 1
        1 2 3 2 1
      1 2 3 4 3 2 1
    1 2 3 4 5 4 3 2 1

    Row i: numbers 1..i then i-1..1 (palindrome row), centered.
    Time Complexity  : O(N²)
    Space Complexity : O(1)
    """

    def __init__(self, n: int):
        self.n = n

    def print_pattern(self):
        for i in range(1, self.n + 1):
            ascending  = list(range(1, i + 1))
            descending = list(range(i - 1, 0, -1))
            row_nums   = ascending + descending
            row_str    = " ".join(str(x) for x in row_nums)
            # padding: each number is 2 chars wide, (n-i) padding units
            pad = " " * ((self.n - i) * 2)
            print(pad + row_str)


n = int(input("Enter number of rows: "))
NumberPyramid(n).print_pattern()
