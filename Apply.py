class Apply:
    def __init__(self, left, right, should_par):
        self.left = left
        self.right = right
        self.should_par = should_par

    def __str__(self):
        if self.should_par:
            return "(" + str(self.left) + " " + str(self.right) + ")"
        else:
            return str(self.left) + " " + str(self.right)

    def __eq__(self, other):
        if isinstance(other, Apply):
            return self.left == other.left and self.right == other.right
        return False

    def __hash__(self):
        return hash((self.left, self.right))
