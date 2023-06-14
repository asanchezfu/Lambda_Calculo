from Abstraction import *
from Variable import *
from RecFunction import *
from Calcul import *


class Value:
    def __init__(self, value):
        self.value = value

    def as_integer(self):
        return int(self.value)

    def as_string(self):
        return str(self.value)

    def as_abstraction(self):
        return self.value

    def as_rec(self):
        return self.value

    def as_if_stat(self):
        return self.value

    def as_calcul(self):
        return self.value

    def is_integer(self):
        return isinstance(self.value, int)

    def is_abstraction(self):
        return isinstance(self.value, Abstraction)

    def is_variable(self):
        return isinstance(self.value, Variable)

    def is_string(self):
        return isinstance(self.value, str)

    def is_rec(self):
        return isinstance(self.value, RecFunction)

    def is_calcul(self):
        return isinstance(self.value, Calcul)

    def __eq__(self, other):
        if isinstance(other, Value):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        return str(self.value)

    def check_continue(self):
        return not (self.is_abstraction() or self.is_variable() or self.is_integer())