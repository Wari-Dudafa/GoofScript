from src import tokenize
from src import syntaxAnalysis
from src import interpret

import sys

path = sys.argv[1]


def main():

  with open("./tests/" + path + ".goof", "r") as file:
    content = file.read()
    tokens = tokenize.Tokenize(content.replace("\n", " "))
    syntax_tree = syntaxAnalysis.SyntaxAnalysis(tokens)

    if syntax_tree[0]:
      interpret.Interpret(syntax_tree[1], True)


main()
