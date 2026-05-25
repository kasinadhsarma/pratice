class InvertedTriangle:
    """
    Pattern (n=5):
    1 2 3 4 5
    1 2 3 4
    1 2 3
    1 2
    1

    Rows decrease from n down to 1.
    Time Complexity  : O(N²)
    Space Complexity : O(1)
    """

    def __init__(self, n: int):
        self.n = n

    def print_pattern(self):
        for i in range(self.n, 0, -1):
            print(" ".join(str(j) for j in range(1, i + 1)))


n = int(input("Enter number of rows: "))
InvertedTriangle(n).print_pattern()
