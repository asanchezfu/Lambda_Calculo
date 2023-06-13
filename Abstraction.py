class Abstraction:
    def init(self, var, exp, is_inside):
        self.var = var
        self.exp = exp
        self.is_inside = is_inside

    def get_var(self):
        return self.var

    def get_exp(self):
        return self.exp

    def set_exp(self, exp):
        self.exp = exp

    def is_inside(self):
        return self.is_inside

    def set_inside(self, is_inside):
        self.is_inside = is_inside

    def str(self):
        if self.is_inside:
            return "λ" + self.var + "." + str(self.exp)
        else:
            return "(λ" + self.var + "." + str(self.exp) + ")"

    def can_apply(self):
        return bool(re.search(r"\b" + self.var + r"\b", str(self.exp)))