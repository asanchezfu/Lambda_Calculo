class Calcul:
    def __init__(self, left, operateur, right):
        self.left = left
        self.operateur = operateur
        self.right = right

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_operateur(self):
        return self.operateur

    def __eq__(self, other):
        if isinstance(other, Calcul):
            return (
                self.left == other.left
                and self.operateur == other.operateur
                and self.right == other.right
            )
        return False

    def __hash__(self):
        return hash((self.left, self.operateur, self.right))

    def __str__(self):
        return str(self.left) + self.operateur + str(self.right)
