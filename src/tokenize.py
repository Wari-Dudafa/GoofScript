import constants


def Tokenize(content):
  tokens = content.split(" ")
  tokens_array = []

  for token in tokens:

    if token in constants.ALL_TOKENS:
      tokens_array.append([token, token, True])
    else:
      tokens_array.append(["not_token", token, False])

    if token[-1] == ";":
      tokens_array.pop()
      tokens_array.append(["not_token", token[0:len(token) - 1], False])
      tokens_array.append([";", ";", True])
  return tokens_array
