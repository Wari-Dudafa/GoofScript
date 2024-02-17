import tokenize
import syntaxAnalysis


def main():

  with open("test.goof", "r") as file:
    content = file.read()
    tokens = tokenize.Tokenize(content.replace("\n", " "))
    syntax_analysis = syntaxAnalysis.SyntaxAnalysis(tokens)

    if syntax_analysis[0]:
      print("Syntax Analysis: OK")
      print(syntax_analysis[1])




main()
