class IfStat:
    def __init__(self, leftToEq, rightToEq, thenReturn, elseReturn, operator):
        self.leftToEq = leftToEq
        self.rightToEq = rightToEq
        self.thenReturn = thenReturn
        self.elseReturn = elseReturn
        self.operator = operator

    def get_left_to_eq(self):
        return self.leftToEq

    def get_right_to_eq(self):
        return self.rightToEq

    def get_then_return(self):
        return self.thenReturn

    def get_else_return(self):
        return self.elseReturn

    def get_operator(self):
        return self.operator

    def __eq__(self, other):
        if isinstance(other, IfStat):
            return (
                self.leftToEq == other.leftToEq
                and self.rightToEq == other.rightToEq
                and self.thenReturn == other.thenReturn
                and self.elseReturn == other.elseReturn
                and self.operator == other.operator
            )
        return False

    def __hash__(self):
        return hash((self.leftToEq, self.rightToEq, self.thenReturn, self.elseReturn, self.operator))

    def __str__(self):
        return "if(" + str(self.leftToEq) + self.operator + str(self.rightToEq) + ")then{" + str(
            self.thenReturn) + "}else{" + str(self.elseReturn) + "}"
