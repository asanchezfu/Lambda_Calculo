# Generated from proyectoLambda.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,23,52,2,0,7,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,3,0,36,8,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,5,0,47,8,0,10,0,12,0,50,9,0,1,0,0,1,0,1,0,0,2,1,0,10,15,1,0,
        6,7,58,0,35,1,0,0,0,2,3,6,0,-1,0,3,4,5,3,0,0,4,5,3,0,0,0,5,6,5,2,
        0,0,6,36,1,0,0,0,7,36,5,20,0,0,8,36,5,21,0,0,9,10,5,16,0,0,10,11,
        5,3,0,0,11,12,3,0,0,0,12,13,7,0,0,0,13,14,3,0,0,0,14,15,5,2,0,0,
        15,16,5,17,0,0,16,17,5,5,0,0,17,18,3,0,0,0,18,19,5,4,0,0,19,20,5,
        18,0,0,20,21,5,5,0,0,21,22,3,0,0,0,22,23,5,4,0,0,23,36,1,0,0,0,24,
        25,5,22,0,0,25,26,5,20,0,0,26,27,5,9,0,0,27,36,3,0,0,2,28,29,5,19,
        0,0,29,30,5,1,0,0,30,31,5,20,0,0,31,32,5,1,0,0,32,33,5,20,0,0,33,
        34,5,9,0,0,34,36,3,0,0,1,35,2,1,0,0,0,35,7,1,0,0,0,35,8,1,0,0,0,
        35,9,1,0,0,0,35,24,1,0,0,0,35,28,1,0,0,0,36,48,1,0,0,0,37,38,10,
        6,0,0,38,39,5,8,0,0,39,47,3,0,0,7,40,41,10,5,0,0,41,42,7,1,0,0,42,
        47,3,0,0,6,43,44,10,3,0,0,44,45,5,1,0,0,45,47,3,0,0,4,46,37,1,0,
        0,0,46,40,1,0,0,0,46,43,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,
        1,0,0,0,49,1,1,0,0,0,50,48,1,0,0,0,3,35,46,48
    ]

class proyectoLambdaParser ( Parser ):

    grammarFileName = "proyectoLambda.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "' '", "')'", "'('", "'}'", "'{'", "'+'", 
                     "'-'", "'*'", "'.'", "'='", "'!='", "'>'", "'<'", "'>='", 
                     "'<='", "'if'", "'then'", "'else'", "'rec'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "RPAR", "LPAR", "RCURL", 
                      "LCURL", "PLUS", "MINUS", "MULT", "DOT", "EQ", "NEQ", 
                      "GT", "LT", "GTEQ", "LTEQ", "IF", "THEN", "ELSE", 
                      "REC", "VAR", "INT", "LAMBDA", "WS" ]

    RULE_expression = 0

    ruleNames =  [ "expression" ]

    EOF = Token.EOF
    T__0=1
    RPAR=2
    LPAR=3
    RCURL=4
    LCURL=5
    PLUS=6
    MINUS=7
    MULT=8
    DOT=9
    EQ=10
    NEQ=11
    GT=12
    LT=13
    GTEQ=14
    LTEQ=15
    IF=16
    THEN=17
    ELSE=18
    REC=19
    VAR=20
    INT=21
    LAMBDA=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return proyectoLambdaParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a proyectoLambdaParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(proyectoLambdaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(proyectoLambdaParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(proyectoLambdaParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(proyectoLambdaParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)


    class MultContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a proyectoLambdaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(proyectoLambdaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(proyectoLambdaParser.ExpressionContext,i)

        def MULT(self):
            return self.getToken(proyectoLambdaParser.MULT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMult" ):
                listener.enterMult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMult" ):
                listener.exitMult(self)


    class ApplicationContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a proyectoLambdaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(proyectoLambdaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(proyectoLambdaParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterApplication" ):
                listener.enterApplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitApplication" ):
                listener.exitApplication(self)


    class RecRuleContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a proyectoLambdaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REC(self):
            return self.getToken(proyectoLambdaParser.REC, 0)
        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(proyectoLambdaParser.VAR)
            else:
                return self.getToken(proyectoLambdaParser.VAR, i)
        def DOT(self):
            return self.getToken(proyectoLambdaParser.DOT, 0)
        def expression(self):
            return self.getTypedRuleContext(proyectoLambdaParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecRule" ):
                listener.enterRecRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecRule" ):
                listener.exitRecRule(self)


    class AbstractionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a proyectoLambdaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LAMBDA(self):
            return self.getToken(proyectoLambdaParser.LAMBDA, 0)
        def VAR(self):
            return self.getToken(proyectoLambdaParser.VAR, 0)
        def DOT(self):
            return self.getToken(proyectoLambdaParser.DOT, 0)
        def expression(self):
            return self.getTypedRuleContext(proyectoLambdaParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbstraction" ):
                listener.enterAbstraction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbstraction" ):
                listener.exitAbstraction(self)


    class VariableContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a proyectoLambdaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(proyectoLambdaParser.VAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)


    class IfRuleContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a proyectoLambdaParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(proyectoLambdaParser.IF, 0)
        def LPAR(self):
            return self.getToken(proyectoLambdaParser.LPAR, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(proyectoLambdaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(proyectoLambdaParser.ExpressionContext,i)

        def RPAR(self):
            return self.getToken(proyectoLambdaParser.RPAR, 0)
        def THEN(self):
            return self.getToken(proyectoLambdaParser.THEN, 0)
        def LCURL(self, i:int=None):
            if i is None:
                return self.getTokens(proyectoLambdaParser.LCURL)
            else:
                return self.getToken(proyectoLambdaParser.LCURL, i)
        def RCURL(self, i:int=None):
            if i is None:
                return self.getTokens(proyectoLambdaParser.RCURL)
            else:
                return self.getToken(proyectoLambdaParser.RCURL, i)
        def ELSE(self):
            return self.getToken(proyectoLambdaParser.ELSE, 0)
        def EQ(self):
            return self.getToken(proyectoLambdaParser.EQ, 0)
        def NEQ(self):
            return self.getToken(proyectoLambdaParser.NEQ, 0)
        def GT(self):
            return self.getToken(proyectoLambdaParser.GT, 0)
        def LT(self):
            return self.getToken(proyectoLambdaParser.LT, 0)
        def GTEQ(self):
            return self.getToken(proyectoLambdaParser.GTEQ, 0)
        def LTEQ(self):
            return self.getToken(proyectoLambdaParser.LTEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfRule" ):
                listener.enterIfRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfRule" ):
                listener.exitIfRule(self)


    class ParenExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a proyectoLambdaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(proyectoLambdaParser.LPAR, 0)
        def expression(self):
            return self.getTypedRuleContext(proyectoLambdaParser.ExpressionContext,0)

        def RPAR(self):
            return self.getToken(proyectoLambdaParser.RPAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpression" ):
                listener.enterParenExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpression" ):
                listener.exitParenExpression(self)


    class IntegerContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a proyectoLambdaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(proyectoLambdaParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = proyectoLambdaParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = proyectoLambdaParser.ParenExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 3
                self.match(proyectoLambdaParser.LPAR)
                self.state = 4
                self.expression(0)
                self.state = 5
                self.match(proyectoLambdaParser.RPAR)
                pass
            elif token in [20]:
                localctx = proyectoLambdaParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 7
                self.match(proyectoLambdaParser.VAR)
                pass
            elif token in [21]:
                localctx = proyectoLambdaParser.IntegerContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 8
                self.match(proyectoLambdaParser.INT)
                pass
            elif token in [16]:
                localctx = proyectoLambdaParser.IfRuleContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                self.match(proyectoLambdaParser.IF)
                self.state = 10
                self.match(proyectoLambdaParser.LPAR)
                self.state = 11
                self.expression(0)
                self.state = 12
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 64512) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 13
                self.expression(0)
                self.state = 14
                self.match(proyectoLambdaParser.RPAR)
                self.state = 15
                self.match(proyectoLambdaParser.THEN)
                self.state = 16
                self.match(proyectoLambdaParser.LCURL)
                self.state = 17
                self.expression(0)
                self.state = 18
                self.match(proyectoLambdaParser.RCURL)
                self.state = 19
                self.match(proyectoLambdaParser.ELSE)
                self.state = 20
                self.match(proyectoLambdaParser.LCURL)
                self.state = 21
                self.expression(0)
                self.state = 22
                self.match(proyectoLambdaParser.RCURL)
                pass
            elif token in [22]:
                localctx = proyectoLambdaParser.AbstractionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.match(proyectoLambdaParser.LAMBDA)
                self.state = 25
                self.match(proyectoLambdaParser.VAR)
                self.state = 26
                self.match(proyectoLambdaParser.DOT)
                self.state = 27
                self.expression(2)
                pass
            elif token in [19]:
                localctx = proyectoLambdaParser.RecRuleContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 28
                self.match(proyectoLambdaParser.REC)
                self.state = 29
                self.match(proyectoLambdaParser.T__0)
                self.state = 30
                self.match(proyectoLambdaParser.VAR)
                self.state = 31
                self.match(proyectoLambdaParser.T__0)
                self.state = 32
                self.match(proyectoLambdaParser.VAR)
                self.state = 33
                self.match(proyectoLambdaParser.DOT)
                self.state = 34
                self.expression(1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 48
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 46
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = proyectoLambdaParser.MultContext(self, proyectoLambdaParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 37
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 38
                        self.match(proyectoLambdaParser.MULT)
                        self.state = 39
                        self.expression(7)
                        pass

                    elif la_ == 2:
                        localctx = proyectoLambdaParser.AddContext(self, proyectoLambdaParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 40
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 41
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==6 or _la==7):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 42
                        self.expression(6)
                        pass

                    elif la_ == 3:
                        localctx = proyectoLambdaParser.ApplicationContext(self, proyectoLambdaParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 43
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 44
                        self.match(proyectoLambdaParser.T__0)
                        self.state = 45
                        self.expression(4)
                        pass

             
                self.state = 50
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




