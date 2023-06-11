import sys
from antlr4 import *
from proyectoLambdaLexer import proyectoLambdaLexer
from proyectoLambdaParser import proyectoLambdaParser
 
def main(argv):
    input_stream = FileStream('entrada.txt', encoding='utf-8')
    lexer = proyectoLambdaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = proyectoLambdaParser(stream)
    tree = parser.expression()
    print(tree.toStringTree(recog=parser))
    print("Está bien")
 
if __name__ == '__main__':
    main(sys.argv)
