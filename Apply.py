class Apply:
    def init(self, left, right, should_par):
        self.left = left
        self.right = right
        self.should_par = should_par

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def str(self):
        if self.should_par:
            return "(" + str(self.left) + " " + str(self.right) + ")"
        else:
            return str(self.left) + " " + str(self.right)

    def eq(self, other):
        if isinstance(other, Apply):
            return self.left == other.left and self.right == other.right
        return False

    def hash(self):
        return hash((self.left, self.right))