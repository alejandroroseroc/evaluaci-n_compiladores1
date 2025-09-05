# Generated from IfElseLang.g4 by ANTLR 4.13.1
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
        4,1,17,62,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,0,1,0,1,1,1,1,3,1,24,8,1,1,2,1,2,
        1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,5,3,37,8,3,10,3,12,3,40,9,3,
        1,3,1,3,1,3,1,3,5,3,46,8,3,10,3,12,3,49,9,3,1,3,3,3,52,8,3,1,4,1,
        4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,2,1,0,15,16,
        1,0,8,13,59,0,15,1,0,0,0,2,23,1,0,0,0,4,25,1,0,0,0,6,30,1,0,0,0,
        8,53,1,0,0,0,10,57,1,0,0,0,12,59,1,0,0,0,14,16,3,2,1,0,15,14,1,0,
        0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,19,1,0,0,0,19,20,
        5,0,0,1,20,1,1,0,0,0,21,24,3,4,2,0,22,24,3,6,3,0,23,21,1,0,0,0,23,
        22,1,0,0,0,24,3,1,0,0,0,25,26,5,15,0,0,26,27,5,14,0,0,27,28,3,10,
        5,0,28,29,5,7,0,0,29,5,1,0,0,0,30,31,5,1,0,0,31,32,5,3,0,0,32,33,
        3,8,4,0,33,34,5,4,0,0,34,38,5,5,0,0,35,37,3,2,1,0,36,35,1,0,0,0,
        37,40,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,41,1,0,0,0,40,38,1,
        0,0,0,41,51,5,6,0,0,42,43,5,2,0,0,43,47,5,5,0,0,44,46,3,2,1,0,45,
        44,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,
        0,49,47,1,0,0,0,50,52,5,6,0,0,51,42,1,0,0,0,51,52,1,0,0,0,52,7,1,
        0,0,0,53,54,3,10,5,0,54,55,3,12,6,0,55,56,3,10,5,0,56,9,1,0,0,0,
        57,58,7,0,0,0,58,11,1,0,0,0,59,60,7,1,0,0,60,13,1,0,0,0,5,17,23,
        38,47,51
    ]

class IfElseLangParser ( Parser ):

    grammarFileName = "IfElseLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'('", "')'", "'{'", 
                     "'}'", "';'", "'=='", "'>='", "'<='", "'!='", "'>'", 
                     "'<'", "'='" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "SEMI", "EQ", "GE", "LE", "NE", "GT", "LT", 
                      "ASSIGN", "ID", "NUMBER", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_ifStatement = 3
    RULE_condition = 4
    RULE_expr = 5
    RULE_operator = 6

    ruleNames =  [ "program", "statement", "assignment", "ifStatement", 
                   "condition", "expr", "operator" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    LPAREN=3
    RPAREN=4
    LBRACE=5
    RBRACE=6
    SEMI=7
    EQ=8
    GE=9
    LE=10
    NE=11
    GT=12
    LT=13
    ASSIGN=14
    ID=15
    NUMBER=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(IfElseLangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IfElseLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(IfElseLangParser.StatementContext,i)


        def getRuleIndex(self):
            return IfElseLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = IfElseLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.statement()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==15):
                    break

            self.state = 19
            self.match(IfElseLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(IfElseLangParser.AssignmentContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(IfElseLangParser.IfStatementContext,0)


        def getRuleIndex(self):
            return IfElseLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = IfElseLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.assignment()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.ifStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(IfElseLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(IfElseLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(IfElseLangParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(IfElseLangParser.SEMI, 0)

        def getRuleIndex(self):
            return IfElseLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = IfElseLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(IfElseLangParser.ID)
            self.state = 26
            self.match(IfElseLangParser.ASSIGN)
            self.state = 27
            self.expr()
            self.state = 28
            self.match(IfElseLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(IfElseLangParser.IF, 0)

        def LPAREN(self):
            return self.getToken(IfElseLangParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(IfElseLangParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(IfElseLangParser.RPAREN, 0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(IfElseLangParser.LBRACE)
            else:
                return self.getToken(IfElseLangParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(IfElseLangParser.RBRACE)
            else:
                return self.getToken(IfElseLangParser.RBRACE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IfElseLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(IfElseLangParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(IfElseLangParser.ELSE, 0)

        def getRuleIndex(self):
            return IfElseLangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = IfElseLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(IfElseLangParser.IF)
            self.state = 31
            self.match(IfElseLangParser.LPAREN)
            self.state = 32
            self.condition()
            self.state = 33
            self.match(IfElseLangParser.RPAREN)
            self.state = 34
            self.match(IfElseLangParser.LBRACE)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==15:
                self.state = 35
                self.statement()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
            self.match(IfElseLangParser.RBRACE)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 42
                self.match(IfElseLangParser.ELSE)
                self.state = 43
                self.match(IfElseLangParser.LBRACE)
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1 or _la==15:
                    self.state = 44
                    self.statement()
                    self.state = 49
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 50
                self.match(IfElseLangParser.RBRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IfElseLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(IfElseLangParser.ExprContext,i)


        def operator(self):
            return self.getTypedRuleContext(IfElseLangParser.OperatorContext,0)


        def getRuleIndex(self):
            return IfElseLangParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = IfElseLangParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.expr()
            self.state = 54
            self.operator()
            self.state = 55
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(IfElseLangParser.ID, 0)

        def NUMBER(self):
            return self.getToken(IfElseLangParser.NUMBER, 0)

        def getRuleIndex(self):
            return IfElseLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = IfElseLangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            _la = self._input.LA(1)
            if not(_la==15 or _la==16):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(IfElseLangParser.GT, 0)

        def LT(self):
            return self.getToken(IfElseLangParser.LT, 0)

        def EQ(self):
            return self.getToken(IfElseLangParser.EQ, 0)

        def GE(self):
            return self.getToken(IfElseLangParser.GE, 0)

        def LE(self):
            return self.getToken(IfElseLangParser.LE, 0)

        def NE(self):
            return self.getToken(IfElseLangParser.NE, 0)

        def getRuleIndex(self):
            return IfElseLangParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)




    def operator(self):

        localctx = IfElseLangParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16128) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





