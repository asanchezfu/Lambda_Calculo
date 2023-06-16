from proyectoLambdaVisitor import proyectoLambdaVisitor
from proyectoLambdaParser import proyectoLambdaParser

class LambdaBasicVisitor(proyectoLambdaVisitor):

    def visitAdd(self, ctx:proyectoLambdaParser.AddContext):
        print("Reconozco la suma")
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left + right
    
    def visitMult(self, ctx:proyectoLambdaParser.AddContext):
        print("Reconozco la multiplicación")
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left, right
    
    
    def visitParenExpression(self, ctx:proyectoLambdaParser.ParenExpressionContext):
        return self.visit(ctx.expression())

    def visitVariable(self, ctx:proyectoLambdaParser.VariableContext):
        return ctx.VAR().getText()

    def visitInteger(self, ctx:proyectoLambdaParser.IntegerContext):
        return int(ctx.getText())


