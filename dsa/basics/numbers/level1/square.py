class Square:
    """
    Pattern (n=5):
    1 2 3 4 5
    1 2 3 4 5
    1 2 3 4 5
    1 2 3 4 5
    1 2 3 4 5

    Every row prints numbers 1..n.
    Time Complexity  : O(N²)
    Space Complexity : O(1)
    """

    def __init__(self, n: int):
        self.n = n

    def print_pattern(self):
        row = " ".join(str(j) for j in range(1, self.n + 1))
        for _ in range(self.n):
            print(row)


n = int(input("Enter size of square: "))
Square(n).print_pattern()
