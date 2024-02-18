from src import tokenize
from src import syntaxAnalysis
from src import interpret

import sys


path = sys.argv[2]

if sys.argv[1] == "test":
  path = "./tests/" + path + ".goof"
elif sys.argv[1] == "prod":
  path = "./" + path + ".goof"


def main():

  with open(path, "r") as file:
    content = file.read()
    tokens = tokenize.Tokenize(content.replace("\n", " "))
    syntax_tree = syntaxAnalysis.SyntaxAnalysis(tokens)

    if syntax_tree[0]:
      interpret.Interpret(syntax_tree[1], True)


main()
