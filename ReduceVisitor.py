from LambdaBasicVisitor import *
from proyectoLambdaParser import proyectoLambdaParser
from Apply import *
from Value import *
from Abstraction import *
from Variable import *
from RecFunction import *
from Calcul import *
from IfStat import *


class ReduceVisitor(LambdaBasicVisitor):
    def __init__(self, freeVars):
        self.replaceMap = {}
        self.freeVars = freeVars

    def visit_variable(self, ctx):
        var = ctx.getText()
        if self.under_abs(ctx):
            if var in self.replaceMap:
                var = self.replaceMap[var]
            return Value(Variable(var))
        else:
            return super().visit_variable(ctx)

    def visit_paren_expression(self, ctx):
        self.replaceMap.clear()
        return super().visit_paren_expression(ctx)

    def visit_abstraction(self, ctx):
        var = ctx.VAR().getText()
        if var in self.freeVars:
            new_var = var
            i = 0
            while new_var in self.freeVars:
                new_var = var + str(i)
                i += 1
            self.replaceMap[var] = new_var
            var = new_var

        expression = self.visit(ctx.expression())

        if isinstance(ctx.parent, proyectoLambdaParser.ParenExpressionContext):
            return Value(Abstraction(var, expression, False))
        else:
            return Value(Abstraction(var, expression, True))

    def visit_application(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        if left.is_rec():
            rec_function = left.as_rec()
            if_stat = rec_function.get_function().as_if_stat()

            new_right = if_stat.get_right_to_eq().replace(rec_function.get_apply_to_var().get_id(), right.as_string())
            new_left = if_stat.get_left_to_eq().replace(rec_function.get_apply_to_var().get_id(), right.as_string())
            replace_then = if_stat.get_then_return().replace(rec_function.get_apply_to_var().get_id(), right.as_string())
            replace_then = replace_then.replace(rec_function.get_func_name_var().get_id(), rec_function.to_string())
            replace_else = if_stat.get_else_return().replace(rec_function.get_apply_to_var().get_id(), right.as_string())
            replace_else = replace_else.replace(rec_function.get_func_name_var().get_id(), rec_function.to_string())

            if_changed = IfStat(Value(new_left), Value(new_right), Value(replace_then), Value(replace_else),
                                if_stat.get_operator())

            return Value(if_changed)

        if not left.is_abstraction():
            if isinstance(ctx.parent, proyectoLambdaParser.ParenExpressionContext):
                return Value(Apply(left, right, True))
            else:
                return Value(Apply(left, right, False))
        else:
            function = left.as_abstraction()
            if function.can_apply():
                if function.get_exp().is_variable():
                    if self.under_abs(ctx):
                        return Value(Apply(left, right, False))
                    return right
                elif function.get_exp().is_abstraction():
                    if right.is_abstraction():
                        right.as_abstraction().set_inside(False)
                    return Value(Abstraction(function.get_var(),
                                             Value(function.get_exp().as_string().replace(function.get_var(),
                                                                                        right.as_string()))))
                elif function.get_exp().is_string():
                    return Value(Apply(left, right, False))
                else:
                    if self.under_abs(ctx):
                        return Value(Apply(left, right, False))
                    return Value(function.get_exp().as_string().replace(function.get_var(), right.as_string()))
            else:
                if function.get_exp().is_string():
                    return Value(Apply(left, right, False))
                return function.get_exp()

    def under_abs(self, ctx):
        parent = ctx.parent
        if parent is None:
            return False
        while parent.parent is not None:
            if isinstance(parent, proyectoLambdaParser.AbstractionContext):
                return True
            parent = parent.parent
        return False
