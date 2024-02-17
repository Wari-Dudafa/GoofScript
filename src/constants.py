ALL_TOKENS = ["function", "class", "if", "for", "else", "true",
              "false", "null", "print", "bool", "int", "str", "not_token", ":"]
BUILT_IN_FUNCTIONS = ["print"]
DATATYPE = ["bool", "int", "str"]
NEXT_TOKEN = {"int": ["not_token"], "not_token": [":"], ":": ["not_token"]}
