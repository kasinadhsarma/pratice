class Square:
    """
    Pattern (n=5):
    *****
    *****
    *****
    *****
    *****

    Time Complexity  : O(N²)
    Space Complexity : O(1)
    """

    def __init__(self, n: int):
        self.n = n

    def print_pattern(self):
        for _ in range(self.n):
            print("*" * self.n)


n = int(input("Enter size of square: "))
Square(n).print_pattern()
