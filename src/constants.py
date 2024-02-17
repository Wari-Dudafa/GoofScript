ALL_TOKENS = [
  "if", "for", "else", "true", "while",
  "false", "null", "print", "bool", "int", "str",
  "not_token", "or", "and", "not",
  ":", "+", "-", "*", "/", ";",
  "(", ")", "=", "<", ">", "<=", ">=", "!="
]
BUILT_IN_FUNCTIONS = [
  "print"
]
DATATYPE = [
  "bool", "int", "str"
]
NEXT_TOKEN = {
  "int": ["not_token", "+"],
  "str": ["not_token" ],
  "bool": ["not_token" ],
  "not_token": [":", "+"],
  ":": ["not_token"],
  "+": ["not_token", "int"]
}
VARIABLE_DECLARATION = ["bool", "int", "str"]
