import constants


def SyntaxAnalysis(tokens):
  next_token = []

  for (i, token) in enumerate(tokens):
    if len(next_token) == 0:
      next_token = constants.NEXT_TOKEN[token[0]]
      continue

    if token[0] == ";":
      next_token = []
      continue

    if token[0] in next_token:
      next_token = constants.NEXT_TOKEN[token[0]]
    else:
      print(f'Syntax Error "{token[1]}"')
      return [False]
  return [True, tokens]
