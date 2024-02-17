import constants

variables = {}


def Interpret(syntax_tree):
  chunks = Chunkize(syntax_tree)

  for chunk in chunks:

    if chunk[0][0] in constants.VARIABLE_DECLARATION:
      Variable(chunk)
    elif chunk[0][0] in constants.BUILT_IN_FUNCTIONS:
      BuiltInFunction(chunk)


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
        variables[name] = HandleMath(chunk)
      elif data_type == "str":

        string_array = chunk[3:len(chunk)]
        string = ""

        for string_chunk in string_array:
          string += string_chunk[1] + " "

        variables[name] = cast(string)
      else:  # it is a bolean
        data = chunk[3][1]
        variables[name] = cast(data)


def HandleMath(chunk):
  expr = chunk[3:len(chunk)]

  if expr[0][1] in variables:
    result = variables[expr[0][1]]
  else:
    result = int(expr[0][1])

  i = 1
  while i < len(expr):
      # Get the operator and the next number
    operator = expr[i][1]

    if expr[0][1] in variables:
      number = variables[expr[i + 1][1]]
    else:
      number = int(expr[i + 1][1])

    # Perform the operation based on the operator
    if operator == "+":
      result += number
    elif operator == "-":
      result -= number
    elif operator == "*":
      result *= number
    elif operator == "/":
      result /= number
    else:
      print(f'Interpretation: Error "Unknown operator"')
      return None
    # Add more operators here if needed

    # Move to the next operator-number pair
    i += 2
  return result


def BuiltInFunction(chunk):
  if chunk[0][0] == "print":
    HandlePrint(chunk)


def HandlePrint(chunk):
  if len(chunk) == 2:
    if chunk[1][1] in variables:
      print(variables[chunk[1][1]])
    else:
      print(chunk[1][1])

  else:
    for i in range(1, len(chunk)):
      if chunk[i][0] == "not_token":
        if chunk[i][1] in variables:
          print(variables[chunk[i][1]], end=" ")
        else:
          print(chunk[i][1], end=" ")
      else:
        print(chunk[i][1], end=" ")
