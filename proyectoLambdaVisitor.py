# Generated from proyectoLambda.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .proyectoLambdaParser import proyectoLambdaParser
else:
    from proyectoLambdaParser import proyectoLambdaParser

# This class defines a complete generic visitor for a parse tree produced by proyectoLambdaParser.

class proyectoLambdaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by proyectoLambdaParser#add.
    def visitAdd(self, ctx:proyectoLambdaParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoLambdaParser#mult.
    def visitMult(self, ctx:proyectoLambdaParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoLambdaParser#application.
    def visitApplication(self, ctx:proyectoLambdaParser.ApplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoLambdaParser#recRule.
    def visitRecRule(self, ctx:proyectoLambdaParser.RecRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoLambdaParser#abstraction.
    def visitAbstraction(self, ctx:proyectoLambdaParser.AbstractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoLambdaParser#variable.
    def visitVariable(self, ctx:proyectoLambdaParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoLambdaParser#ifRule.
    def visitIfRule(self, ctx:proyectoLambdaParser.IfRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoLambdaParser#parenExpression.
    def visitParenExpression(self, ctx:proyectoLambdaParser.ParenExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by proyectoLambdaParser#integer.
    def visitInteger(self, ctx:proyectoLambdaParser.IntegerContext):
        return self.visitChildren(ctx)



del proyectoLambdaParser