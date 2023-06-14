class Variable:
    def __init__(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def __str__(self):
        return self.id

    def __eq__(self, other):
        if isinstance(other, Variable):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)
