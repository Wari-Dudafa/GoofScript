import constants

variables = {}


def Interpret(syntax_tree):
  chunks = Chunkize(syntax_tree)

  for chunk in chunks:

    if chunk[0][0] in constants.VARIABLE_DECLARATION:
      Variable(chunk)

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


def Variable(chunk):
  data_type = chunk[0][0]
  name = chunk[1][1]
  caster = {"int": int, "str": str, "bool": bool}

  if data_type in constants.VARIABLE_DECLARATION:
    if chunk[1][0] == "not_token":
      variables[name] = None
    if chunk[2][0] == ":":
      cast = caster[data_type]

      if data_type == "int":

        expr = chunk[3:len(chunk)]
        result = int(expr[0][1])
        i = 1
        while i < len(expr):
            # Get the operator and the next number
            operator = expr[i][1]
            number = int(expr[i+1][1])
            
            # Perform the operation based on the operator
            if operator == "+":
                result += number
            elif operator == "-":
                result -= number
            # Add more operators here if needed
            
            # Move to the next operator-number pair
            i += 2
        variables[name] = result

      elif data_type == "str":
        data = chunk[3][1]
        variables[name] = cast(data)
      else:  # it is a bolean
        data = chunk[3][1]
        variables[name] = cast(data)
