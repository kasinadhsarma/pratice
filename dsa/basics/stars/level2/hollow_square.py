class HollowSquare:
    """
    Pattern (n=5):
    *****
    *   *
    *   *
    *   *
    *****

    Rule: print '*' only for first/last row or first/last column.
    Time Complexity  : O(N²)
    Space Complexity : O(1)
    """

    def __init__(self, n: int):
        self.n = n

    def print_pattern(self):
        for i in range(1, self.n + 1):
            row = ""
            for j in range(1, self.n + 1):
                if i == 1 or i == self.n or j == 1 or j == self.n:
                    row += "*"
                else:
                    row += " "
            print(row)


n = int(input("Enter size of hollow square: "))
HollowSquare(n).print_pattern()
