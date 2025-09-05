from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl
from IfElseLangLexer import IfElseLangLexer
from IfElseLangParser import IfElseLangParser


code = """a = 10;
b = 20;
if (a > b) {
  max = a;
} else {
  if (a == b) {
    max = a;
  } else {
    max = b;
  }
}
"""

input_stream = InputStream(code)
lexer = IfElseLangLexer(input_stream)
token_stream = CommonTokenStream(lexer)
token_stream.fill()

print("## TOKENS")
for t in token_stream.tokens:
    if t.type != Token.EOF:
        name = lexer.symbolicNames[t.type]
        print(f"{name:<15} '{t.text}' @ {t.line}:{t.column}")


parser = IfElseLangParser(token_stream)
tree = parser.program()

print("\n## ÁRBOL SINTÁCTICO (toStringTree)")
print(tree.toStringTree(recog=parser))

# Pretty print (indentado)
def pretty(node, rule_names, level=0):
    indent = "  " * level
    if isinstance(node, TerminalNodeImpl):
        print(f"{indent}TOKEN({node.getText()})")
    else:
        rule_name = rule_names[node.getRuleIndex()]
        print(f"{indent}{rule_name}")
        for child in node.children or []:
            pretty(child, rule_names, level + 1)

print("\n## ÁRBOL SINTÁCTICO (indentado)")
pretty(tree, parser.ruleNames)
