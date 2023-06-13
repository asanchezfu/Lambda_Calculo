from proyectoLambdaParser import proyectoLambdaParser
from proyectoLambdaVisitor import proyectoLambdaVisitor

class MiProyectoLambdaParser(proyectoLambdaParser, proyectoLambdaVisitor):
    def visit(self, ctx):
        if isinstance(ctx, proyectoLambdaParser.AddContext):
            return self.visitAdd(ctx)
        # Continúa con el comportamiento predeterminado
        return super().visit(ctx)

    def visitAdd(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        # Realizar la operación de suma y retornar el resultado
        return left + right
