import re

class Abstraction:
    def __init__(self, var, expression, is_inside):
        self.var = var
        self.expression = expression
        self.is_inside = is_inside

    def get_var(self):
        return self.var

    def get_expression(self):
        return self.expression

    def set_expression(self, expression):
        self.expression = expression

    def is_inside(self):
        return self.is_inside

    def set_inside(self, is_inside):
        self.is_inside = is_inside

    def __str__(self):
        if self.is_inside:
            return "λ" + self.var + "." + str(self.expression)
        else:
            return "(λ" + self.var + "." + str(self.expression) + ")"

    def can_apply(self):
        return bool(re.search(r"\b" + self.var + r"\b", str(self.expression)))
