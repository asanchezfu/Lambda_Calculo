class RecFunction:
    def __init__(self, func_name_var, apply_to_var, function):
        self.func_name_var = func_name_var
        self.apply_to_var = apply_to_var
        self.function = function

    def get_func_name_var(self):
        return self.func_name_var

    def get_apply_to_var(self):
        return self.apply_to_var

    def get_function(self):
        return self.function

    def __eq__(self, other):
        if isinstance(other, RecFunction):
            return (
                self.func_name_var == other.func_name_var
                and self.apply_to_var == other.apply_to_var
                and self.function == other.function
            )
        return False

    def __hash__(self):
        return hash((self.func_name_var, self.apply_to_var, self.function))

    def __str__(self):
        return "(rec " + str(self.func_name_var) + " " + str(self.apply_to_var) + "." + str(self.function) + ")"
