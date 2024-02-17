import tokenize
import syntaxAnalysis
import interpret


def main():

  with open("test.goof", "r") as file:
    content = file.read()
    tokens = tokenize.Tokenize(content.replace("\n", " "))
    syntax_tree = syntaxAnalysis.SyntaxAnalysis(tokens)

    if syntax_tree[0]:
      print("Syntax Analysis: OK")

      interpret.Interpret(syntax_tree[1])


main()
