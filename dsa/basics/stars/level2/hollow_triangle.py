class HollowTriangle:
    """
    Pattern (n=5):
    *
    **
    * *
    *  *
    *****

    Rule: print '*' only on borders (first col, last col of row, or last row).
    Time Complexity  : O(N²)
    Space Complexity : O(1)
    """

    def __init__(self, n: int):
        self.n = n

    def print_pattern(self):
        for i in range(1, self.n + 1):
            row = ""
            for j in range(1, i + 1):
                if i == self.n or j == 1 or j == i:
                    row += "*"
                else:
                    row += " "
            print(row)


n = int(input("Enter number of rows: "))
HollowTriangle(n).print_pattern()
