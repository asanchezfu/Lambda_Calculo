from LambdaBasicVisitor import *
from proyectoLambdaVisitor import *
from proyectoLambdaParser import proyectoLambdaParser


class FreeVariableVisitor(LambdaBasicVisitor):
    def __init__(self):
        self.freeVars = set()
        self.boundVars = set()

    def get_free_variables(self):
        return self.freeVars

    def visit_abstraction(self, ctx):
        var = ctx.VAR().getText()
        self.boundVars.add(var)
        expression = self.visit(ctx.expression())
        self.boundVars.remove(var)

        if isinstance(ctx.parent, proyectoLambdaParser.ParenExpressionContext):
            return Value(Abstraction(var, expression, False))
        else:
            return Value(Abstraction(var, expression, True))

    def visit_variable(self, ctx):
        var = ctx.getText()
        if var not in self.boundVars:
            self.freeVars.add(var)
        return super().visit_variable(ctx)
