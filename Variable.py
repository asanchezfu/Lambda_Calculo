class Variable:
    def init(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def str(self):
        return self.id

    def eq(self, other):
        if isinstance(other, Variable):
            return self.id == other.id
        return False

    def hash(self):
        return hash(self.id)