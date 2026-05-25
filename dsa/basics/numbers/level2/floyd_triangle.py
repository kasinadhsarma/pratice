class FloydTriangle:
    """
    Pattern (n=5):
    1
    2  3
    4  5  6
    7  8  9  10
    11 12 13 14 15

    Consecutive integers fill each row from left to right.
    Time Complexity  : O(N²)
    Space Complexity : O(1)
    """

    def __init__(self, n: int):
        self.n = n

    def print_pattern(self):
        num = 1
        for i in range(1, self.n + 1):
            row = ""
            for j in range(1, i + 1):
                row += str(num).ljust(4)   # width-4 for alignment
                num += 1
            print(row.rstrip())


n = int(input("Enter number of rows: "))
FloydTriangle(n).print_pattern()
