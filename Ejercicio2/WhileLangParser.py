# Generated from WhileLang.g4 by ANTLR 4.13.1
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
        4,1,22,101,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,22,8,0,11,0,12,0,23,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,
        1,3,1,3,5,3,46,8,3,10,3,12,3,49,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,
        1,4,5,4,59,8,4,10,4,12,4,62,9,4,1,4,1,4,1,4,1,4,5,4,68,8,4,10,4,
        12,4,71,9,4,1,4,3,4,74,8,4,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,
        7,1,8,1,8,1,8,3,8,89,8,8,1,8,1,8,1,8,5,8,94,8,8,10,8,12,8,97,9,8,
        1,9,1,9,1,9,0,1,16,10,0,2,4,6,8,10,12,14,16,18,0,2,1,0,16,19,1,0,
        12,15,101,0,21,1,0,0,0,2,32,1,0,0,0,4,34,1,0,0,0,6,39,1,0,0,0,8,
        52,1,0,0,0,10,75,1,0,0,0,12,78,1,0,0,0,14,81,1,0,0,0,16,88,1,0,0,
        0,18,98,1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,23,1,0,0,0,23,21,
        1,0,0,0,23,24,1,0,0,0,24,25,1,0,0,0,25,26,5,0,0,1,26,1,1,0,0,0,27,
        33,3,4,2,0,28,33,3,6,3,0,29,33,3,8,4,0,30,33,3,10,5,0,31,33,3,12,
        6,0,32,27,1,0,0,0,32,28,1,0,0,0,32,29,1,0,0,0,32,30,1,0,0,0,32,31,
        1,0,0,0,33,3,1,0,0,0,34,35,5,20,0,0,35,36,5,11,0,0,36,37,3,16,8,
        0,37,38,5,10,0,0,38,5,1,0,0,0,39,40,5,1,0,0,40,41,5,6,0,0,41,42,
        3,14,7,0,42,43,5,7,0,0,43,47,5,8,0,0,44,46,3,2,1,0,45,44,1,0,0,0,
        46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,49,47,1,
        0,0,0,50,51,5,9,0,0,51,7,1,0,0,0,52,53,5,2,0,0,53,54,5,6,0,0,54,
        55,3,14,7,0,55,56,5,7,0,0,56,60,5,8,0,0,57,59,3,2,1,0,58,57,1,0,
        0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,63,1,0,0,0,62,60,
        1,0,0,0,63,73,5,9,0,0,64,65,5,3,0,0,65,69,5,8,0,0,66,68,3,2,1,0,
        67,66,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,72,1,
        0,0,0,71,69,1,0,0,0,72,74,5,9,0,0,73,64,1,0,0,0,73,74,1,0,0,0,74,
        9,1,0,0,0,75,76,5,4,0,0,76,77,5,10,0,0,77,11,1,0,0,0,78,79,5,5,0,
        0,79,80,5,10,0,0,80,13,1,0,0,0,81,82,3,16,8,0,82,83,3,18,9,0,83,
        84,3,16,8,0,84,15,1,0,0,0,85,86,6,8,-1,0,86,89,5,20,0,0,87,89,5,
        21,0,0,88,85,1,0,0,0,88,87,1,0,0,0,89,95,1,0,0,0,90,91,10,3,0,0,
        91,92,7,0,0,0,92,94,3,16,8,4,93,90,1,0,0,0,94,97,1,0,0,0,95,93,1,
        0,0,0,95,96,1,0,0,0,96,17,1,0,0,0,97,95,1,0,0,0,98,99,7,1,0,0,99,
        19,1,0,0,0,8,23,32,47,60,69,73,88,95
    ]

class WhileLangParser ( Parser ):

    grammarFileName = "WhileLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'while'", "'if'", "'else'", "'break'", 
                     "'continue'", "'('", "')'", "'{'", "'}'", "';'", "'='", 
                     "'>'", "'<'", "'=='", "'!='", "'+'", "'-'", "'*'", 
                     "'/'" ]

    symbolicNames = [ "<INVALID>", "WHILE", "IF", "ELSE", "BREAK", "CONTINUE", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "SEMI", "ASSIGN", 
                      "GT", "LT", "EQ", "NE", "PLUS", "MINUS", "MULT", "DIV", 
                      "ID", "NUMBER", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_whileStatement = 3
    RULE_ifStatement = 4
    RULE_breakStatement = 5
    RULE_continueStatement = 6
    RULE_condition = 7
    RULE_expr = 8
    RULE_operator = 9

    ruleNames =  [ "program", "statement", "assignment", "whileStatement", 
                   "ifStatement", "breakStatement", "continueStatement", 
                   "condition", "expr", "operator" ]

    EOF = Token.EOF
    WHILE=1
    IF=2
    ELSE=3
    BREAK=4
    CONTINUE=5
    LPAREN=6
    RPAREN=7
    LBRACE=8
    RBRACE=9
    SEMI=10
    ASSIGN=11
    GT=12
    LT=13
    EQ=14
    NE=15
    PLUS=16
    MINUS=17
    MULT=18
    DIV=19
    ID=20
    NUMBER=21
    WS=22

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
            return self.getToken(WhileLangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.StatementContext,i)


        def getRuleIndex(self):
            return WhileLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = WhileLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.statement()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1048630) != 0)):
                    break

            self.state = 25
            self.match(WhileLangParser.EOF)
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
            return self.getTypedRuleContext(WhileLangParser.AssignmentContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(WhileLangParser.WhileStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(WhileLangParser.IfStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(WhileLangParser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(WhileLangParser.ContinueStatementContext,0)


        def getRuleIndex(self):
            return WhileLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = WhileLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.assignment()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.whileStatement()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.ifStatement()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.breakStatement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 31
                self.continueStatement()
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
            return self.getToken(WhileLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(WhileLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(WhileLangParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(WhileLangParser.SEMI, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = WhileLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(WhileLangParser.ID)
            self.state = 35
            self.match(WhileLangParser.ASSIGN)
            self.state = 36
            self.expr(0)
            self.state = 37
            self.match(WhileLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(WhileLangParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(WhileLangParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(WhileLangParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(WhileLangParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(WhileLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(WhileLangParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.StatementContext,i)


        def getRuleIndex(self):
            return WhileLangParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)




    def whileStatement(self):

        localctx = WhileLangParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(WhileLangParser.WHILE)
            self.state = 40
            self.match(WhileLangParser.LPAREN)
            self.state = 41
            self.condition()
            self.state = 42
            self.match(WhileLangParser.RPAREN)
            self.state = 43
            self.match(WhileLangParser.LBRACE)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1048630) != 0):
                self.state = 44
                self.statement()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(WhileLangParser.RBRACE)
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
            return self.getToken(WhileLangParser.IF, 0)

        def LPAREN(self):
            return self.getToken(WhileLangParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(WhileLangParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(WhileLangParser.RPAREN, 0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(WhileLangParser.LBRACE)
            else:
                return self.getToken(WhileLangParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(WhileLangParser.RBRACE)
            else:
                return self.getToken(WhileLangParser.RBRACE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(WhileLangParser.ELSE, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = WhileLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(WhileLangParser.IF)
            self.state = 53
            self.match(WhileLangParser.LPAREN)
            self.state = 54
            self.condition()
            self.state = 55
            self.match(WhileLangParser.RPAREN)
            self.state = 56
            self.match(WhileLangParser.LBRACE)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1048630) != 0):
                self.state = 57
                self.statement()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
            self.match(WhileLangParser.RBRACE)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 64
                self.match(WhileLangParser.ELSE)
                self.state = 65
                self.match(WhileLangParser.LBRACE)
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1048630) != 0):
                    self.state = 66
                    self.statement()
                    self.state = 71
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 72
                self.match(WhileLangParser.RBRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(WhileLangParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(WhileLangParser.SEMI, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_breakStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)




    def breakStatement(self):

        localctx = WhileLangParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(WhileLangParser.BREAK)
            self.state = 76
            self.match(WhileLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(WhileLangParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(WhileLangParser.SEMI, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_continueStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStatement" ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStatement" ):
                listener.exitContinueStatement(self)




    def continueStatement(self):

        localctx = WhileLangParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(WhileLangParser.CONTINUE)
            self.state = 79
            self.match(WhileLangParser.SEMI)
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
                return self.getTypedRuleContexts(WhileLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.ExprContext,i)


        def operator(self):
            return self.getTypedRuleContext(WhileLangParser.OperatorContext,0)


        def getRuleIndex(self):
            return WhileLangParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = WhileLangParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.expr(0)
            self.state = 82
            self.operator()
            self.state = 83
            self.expr(0)
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
            return self.getToken(WhileLangParser.ID, 0)

        def NUMBER(self):
            return self.getToken(WhileLangParser.NUMBER, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.ExprContext,i)


        def PLUS(self):
            return self.getToken(WhileLangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(WhileLangParser.MINUS, 0)

        def MULT(self):
            return self.getToken(WhileLangParser.MULT, 0)

        def DIV(self):
            return self.getToken(WhileLangParser.DIV, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = WhileLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.state = 86
                self.match(WhileLangParser.ID)
                pass
            elif token in [21]:
                self.state = 87
                self.match(WhileLangParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 95
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = WhileLangParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 90
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 91
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 983040) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 92
                    self.expr(4) 
                self.state = 97
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(WhileLangParser.GT, 0)

        def LT(self):
            return self.getToken(WhileLangParser.LT, 0)

        def EQ(self):
            return self.getToken(WhileLangParser.EQ, 0)

        def NE(self):
            return self.getToken(WhileLangParser.NE, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)




    def operator(self):

        localctx = WhileLangParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




