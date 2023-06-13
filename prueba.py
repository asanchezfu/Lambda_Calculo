import sys
from antlr4 import *
from proyectoLambdaLexer import proyectoLambdaLexer
from proyectoLambdaParser import *
from proyectoLambdaVisitor import proyectoLambdaVisitor
 
def main(argv):
    input_stream = FileStream('entrada.txt', encoding='utf-8')
    lexer = proyectoLambdaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = proyectoLambdaParser(stream)
    tree = parser.expression()
    treeString = tree.toStringTree(recog=parser)
    print(treeString)

    visitor = proyectoLambdaVisitor
    result = visitor.visitParenExpression(tree)

    print(result)


if __name__ == '__main__':
    main(sys.argv)
