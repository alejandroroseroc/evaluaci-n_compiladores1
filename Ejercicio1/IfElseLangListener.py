# Generated from IfElseLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .IfElseLangParser import IfElseLangParser
else:
    from IfElseLangParser import IfElseLangParser

# This class defines a complete listener for a parse tree produced by IfElseLangParser.
class IfElseLangListener(ParseTreeListener):

    # Enter a parse tree produced by IfElseLangParser#program.
    def enterProgram(self, ctx:IfElseLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#program.
    def exitProgram(self, ctx:IfElseLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#statement.
    def enterStatement(self, ctx:IfElseLangParser.StatementContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#statement.
    def exitStatement(self, ctx:IfElseLangParser.StatementContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#assignment.
    def enterAssignment(self, ctx:IfElseLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#assignment.
    def exitAssignment(self, ctx:IfElseLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#ifStatement.
    def enterIfStatement(self, ctx:IfElseLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#ifStatement.
    def exitIfStatement(self, ctx:IfElseLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#condition.
    def enterCondition(self, ctx:IfElseLangParser.ConditionContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#condition.
    def exitCondition(self, ctx:IfElseLangParser.ConditionContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#expr.
    def enterExpr(self, ctx:IfElseLangParser.ExprContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#expr.
    def exitExpr(self, ctx:IfElseLangParser.ExprContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#operator.
    def enterOperator(self, ctx:IfElseLangParser.OperatorContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#operator.
    def exitOperator(self, ctx:IfElseLangParser.OperatorContext):
        pass



del IfElseLangParser