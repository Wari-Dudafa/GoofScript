ALL_TOKENS = [
  "if", "endif", "for", "else", "true", "while", "endwhile",
  "false", "print", "bool", "int", "str",
  "not_token", "or", "and", "not",
  ":", "+", "-", "*", "/", ";",
  "=", "<", ">", "<=", ">=", "!=",
]
BUILT_IN_FUNCTIONS = [
  "print"
]
DATATYPE = [
  "bool", "int", "str"
]
VARIABLE_DECLARATION = ["bool", "int", "str"]
MATHS = ["+", "-", "*", "/"]
COMPARATORS = ["<", ">", "<=", ">=", "!=", "="]
NEXT_TOKEN = {
  "not_token": ALL_TOKENS,
  "int": ["not_token"] + MATHS,
  "str": ["not_token"],
  "bool": ["not_token"],
  ":": ["not_token"],
  "+": ["not_token"],
  "-": ["not_token"],
  "*": ["not_token"],
  "/": ["not_token"],
  "print": ["not_token"],
  "if": ["not_token"],
  "else": [";"],
  "endif": [";"],
  "while": ["not_token"],
  "endwhile": [";"],
  "<": ["not_token"],
  "=": ["not_token"],
  ">": ["not_token"],
  "<=": ["not_token"],
  ">=": ["not_token"],
  "!=": ["not_token"],
}
