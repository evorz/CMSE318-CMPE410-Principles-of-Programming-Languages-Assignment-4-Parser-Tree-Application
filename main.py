class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children


def lex():
    global next_token
    next_token = file.read(1)
    while next_token.isspace():
        next_token = file.read(1)


def unconsumed_input():
    return file.read()


def G():
    ast = E()
    if next_token == '$':
        print("Parsing Successful.")
        return ast
    else:
        print("Parsing Error.")


def E():
    ast = R()
    while next_token == '+':
        lex()
        ast = Node('+', [ast, R()])
    return ast


def R():
    ast = T()
    while next_token == '*':
        lex()
        ast = Node('*', [ast, T()])
    return ast


def T():
    ast = F()
    if next_token == '^':
        lex()
        ast = Node('^', [ast, F()])
    return ast


def F():
    if next_token.isdigit():
        node = Node(int(next_token), [])
        lex()
        return node
    elif next_token == '(':
        lex()
        node = E()
        if next_token == ')':
            lex()
            return node
        else:
            print("Error: Missing closing parenthesis.")
            raise SyntaxError("Parsing Error")
    else:
        print("Error: Invalid token.")
        raise SyntaxError("Parsing Error")


def N(node):
    if node.children:
        for child in node.children:
            N(child)
        if node.value == '+':
            node.value = sum(child.value for child in node.children)
        elif node.value == '*':
            node.value = 1
            for child in node.children:
                node.value *= child.value
        elif node.value == '^':
            node.value = node.children[0].value ** node.children[1].value


next_token = ''
file_name = input("Enter the file name: ")

try:
    with open(file_name, 'r') as file:
        lex()
        ast = G()
        if ast:
            N(ast)
            print("Abstract Syntax Tree:")
            print(ast.value)
            print("Value of the expression:", ast.value)
except FileNotFoundError:
    print("File not found.")
