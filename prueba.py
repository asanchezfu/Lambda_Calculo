import sys
from antlr4 import *
from proyectoLambdaLexer import proyectoLambdaLexer
from proyectoLambdaParser import *
from proyectoLambdaVisitor import proyectoLambdaVisitor
from ReduceVisitor import ReduceVisitor
from FreeVariableVisitor import FreeVariableVisitor

def main(argv):
    input_stream = FileStream('entrada.txt', encoding='utf-8')
    lexer = proyectoLambdaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = proyectoLambdaParser(stream)
    tree = parser.expression()

    freeVariableVisitor = FreeVariableVisitor()
    freeVariableVisitor.visit(tree)
    visitor = ReduceVisitor(freeVariableVisitor.get_free_variables())
    result = visitor.visit(tree)

    print(result)


if __name__ == '__main__':
    main(sys.argv)
