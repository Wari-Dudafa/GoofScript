import lexer;

def main():

  content = ""

  with open("test.goof", "r") as file:
    content = file.read()
    print(content)


main()
