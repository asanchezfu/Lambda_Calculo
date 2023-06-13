import sys
from antlr4 import *
from proyectoLambdaLexer import proyectoLambdaLexer
from proyectoLambdaParser import proyectoLambdaParser
from miProyectoLambdaParser import *
 
def main(argv):
    input_stream = FileStream('entrada.txt', encoding='utf-8')
    lexer = proyectoLambdaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiProyectoLambdaParser(stream)
    tree = parser.expression()
    print(tree.toStringTree(recog=parser))

    result = parser.visit(tree)  # Ejecutar el árbol de análisis sintáctico
    print("Resultado:", result)
 
if __name__ == '__main__':
    main(sys.argv)