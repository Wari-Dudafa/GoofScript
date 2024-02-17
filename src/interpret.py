import constants


def Interpret(syntax_tree):
  variables = {}
  chunks = Chunkize(syntax_tree)

  for chunk in chunks:
    caster = {"int": int, "str": str, "bool": bool}

    if chunk[0][0] in constants.VARIABLE_DECLARATION:
      if chunk[1][0] == "not_token":
        variables[chunk[1][1]] = None
      if chunk[2][0] == ":" and chunk[3][0] == "not_token":
        cast = caster[chunk[0][0]]
        data = chunk[3][1]

        if data != "x":
          variables[chunk[1][1]] = cast(data)

  print(variables)


def Chunkize(syntax_tree):
  current_chunk = []
  chunks = []

  for statement in syntax_tree:
    current_chunk.append(statement)

    if statement[0] == ';':
      current_chunk.pop()
      chunks.append(current_chunk)
      current_chunk = []

  return chunks
