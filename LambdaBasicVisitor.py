from proyectoLambdaVisitor import proyectoLambdaVisitor
from proyectoLambdaParser import proyectoLambdaParser
from Apply import *
from Value import *

class LambdaBasicVisitor(proyectoLambdaVisitor):
    def visitApplication(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if isinstance(ctx.parent, proyectoLambdaParser.ParenExpressionContext):
            return Value(Apply(left.value, right.value, True))
        else:
            return Value(Apply(left.value, right.value, False))

    def visitAbstraction(self, ctx):
        varUnderLambda = ctx.VAR().getText()
        expression = self.visit(ctx.expression())
        if isinstance(ctx.parent, proyectoLambdaParser.ParenExpressionContext):
            return Value(Abstraction(varUnderLambda, expression.value, False))
        else:
            return Value(Abstraction(varUnderLambda, expression.value, True))

    def visitVariable(self, ctx):
        return Value(Variable(ctx.getText()))

    def visitIfRule(self, ctx):
        leftToCheck = self.visit(ctx.expression(0))
        rightToCheck = self.visit(ctx.expression(1))

        if leftToCheck.is_integer() and rightToCheck.is_integer():
            left = leftToCheck.as_integer()
            right = rightToCheck.as_integer()
            op_type = ctx.op.type

            if op_type == proyectoLambdaParser.EQ:
                if left == right:
                    true_return = self.visit(ctx.expression(2))
                    return Value(true_return.value)
                else:
                    false_return = self.visit(ctx.expression(3))
                    return Value(false_return.value)

            elif op_type == proyectoLambdaParser.GT:
                if left > right:
                    true_return = self.visit(ctx.expression(2))
                    return Value(true_return.value)
                else:
                    false_return = self.visit(ctx.expression(3))
                    return Value(false_return.value)

            elif op_type == proyectoLambdaParser.LT:
                if left < right:
                    true_return = self.visit(ctx.expression(2))
                    return Value(true_return.value)
                else:
                    false_return = self.visit(ctx.expression(3))
                    return Value(false_return.value)

            elif op_type == proyectoLambdaParser.GTEQ:
                if left >= right:
                    true_return = self.visit(ctx.expression(2))
                    return Value(true_return.value)
                else:
                    false_return = self.visit(ctx.expression(3))
                    return Value(false_return.value)

            elif op_type == proyectoLambdaParser.LTEQ:
                if left <= right:
                    true_return = self.visit(ctx.expression(2))
                    return Value(true_return.value)
                else:
                    false_return = self.visit(ctx.expression(3))
                    return Value(false_return.value)

            elif op_type == proyectoLambdaParser.NEQ:
                if left != right:
                    true_return = self.visit(ctx.expression(2))
                    return Value(true_return.value)
                else:
                    false_return = self.visit(ctx.expression(3))
                    return Value(false_return.value)

            else:
                raise Exception("L'opérateur de l'expression est inconnu (mais cela ne devrait pas arriver)")

        else:
            return Value(IfStat(leftToCheck, rightToCheck, self.visit(ctx.expression(2)), self.visit(ctx.expression(3)), ctx.op.getText()))

    def visitRecRule(self, ctx):
        func_name = ctx.VAR(0).getText()
        apply_var = ctx.VAR(1).getText()
        function = self.visit(ctx.expression())

        return Value(RecFunction(Variable(func_name), Variable(apply_var), function.value))

    def visitParenExpression(self, ctx):
        return self.visit(ctx.expression())

    def visitInteger(self, ctx):
        return Value(int(ctx.getText()))

    def visitMult(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        if left.is_integer() and right.is_integer():
            return Value(left.as_integer() * right.as_integer())
        else:
            return Value(Calcul(Value(left), '*', Value(right)))

    def visitAdd(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        op_type = ctx.op.type

        if op_type == proyectoLambdaParser.PLUS:
            if left.is_integer() and right.is_integer():
                return Value(left.as_integer() + right.as_integer())
            else:
                return Value(Calcul(Value(left), '+', Value(right)))

        elif op_type == proyectoLambdaParser.MINUS:
            if left.is_integer() and right.is_integer():
                return Value(left.as_integer() - right.as_integer())
            else:
                return Value(Calcul(Value(left), '-', Value(right)))

        else:
            raise Exception("L'opérateur de l'expression est inconnu (mais cela ne devrait pas arriver)")
