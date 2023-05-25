class Node:
    def __init__(self, symbol, leftChild=None, rightChild=None):
        self.symbol = symbol
        self.leftChild = leftChild
        self.rightChild = rightChild

def lex():
    global next_token
    next_token = input_file.read(1)
    while next_token.isspace():
        next_token = input_file.read(1)
    if not next_token:
        next_token = '$'  # Handle end of file

def unconsumed_input():
    return input_file.read()

def G():
    global error
    if error:
        return None
    lex()
    print("G -> E")
    tree = E()
    if next_token == '$' and not error:
        print("success")
        return tree
    else:
        print("failure: unconsumed input =", unconsumed_input())
        return None

def E():
    global error
    if error:
        return None
    print("E -> T R")
    temp = T()
    return R(temp)

def R(tree):
    global error
    if error:
        return None
    if next_token == '+':
        print("R -> + T R")
        lex()
        temp1 = T()
        temp2 = R(temp1)
        return Node('+', tree, temp2)
    elif next_token == '-':
        print("R -> - T R")
        lex()
        temp1 = T()
        temp2 = R(temp1)
        return Node('-', tree, temp2)
    else:
        print("R -> ε")
        return tree

def T():
    global error
    if error:
        return None
    print("T -> F S")
    temp = F()
    return S(temp)

def S(tree):
    global error
    if error:
        return None
    if next_token == '*':
        print("S -> * F S")
        lex()
        temp1 = F()
        temp2 = S(temp1)
        return Node('*', tree, temp2)
    elif next_token == '/':
        print("S -> / F S")
        lex()
        temp1 = F()
        temp2 = S(temp1)
        return Node('/', tree, temp2)
    else:
        print("S -> ε")
        return tree

def F():
    global error
    if error:
        return None
    if next_token == '(':
        print("F -> ( E )")
        lex()
        temp = E()
        if next_token == ')':
            lex()
            return temp
        else:
            error = True
            print("error: unexpected token", next_token)
            print("unconsumed_input =", unconsumed_input())
            return None
    elif next_token in ['a', 'b', 'c', 'd']:
        print("F -> M")
        return M()
    elif next_token in ['0', '1', '2', '3']:
        print("F -> N")
        return N()
    else:
        error = True
        print("error: unexpected token", next_token)
        print("unconsumed_input =", unconsumed_input())
        return None

def M():
    global error, next_token
    prev_token = next_token
    if error:
        return None
    if next_token in ['a', 'b', 'c', 'd']:
        print("M ->", next_token)
        lex()
        return Node(prev_token)
    else:
        error = True
        print("error: unexpected token", next_token)
        print("unconsumed_input =", unconsumed_input())
        return None

def N():
    global error, next_token
    prev_token = next_token
    if error:
        return None
    if next_token in ['0', '1', '2', '3']:
        print("N ->", next_token)
        lex()
        return Node(prev_token)
    else:
        error = True
        print("error: unexpected token", next_token)
        print("unconsumed_input =", unconsumed_input())
        return None

def printTree(tree, level=0):
    if tree is None:
        return

    print(' ' * (4 * level) + tree.symbol)

    if tree.leftChild is not None:
        print(' ' * (4 * level) + '/')
        printTree(tree.leftChild, level + 1)

    if tree.rightChild is not None:
        print(' ' * (4 * level) + '\\')
        printTree(tree.rightChild, level + 1)




def evaluate(tree):
    if tree is None:
        return -1
    if tree.symbol == 'a':
        return 10
    if tree.symbol == 'b':
        return 20
    if tree.symbol == 'c':
        return 30
    if tree.symbol == 'd':
        return 40
    if tree.symbol in ['0', '1', '2', '3']:
        return int(tree.symbol)
    if tree.symbol == '+':
        return evaluate(tree.leftChild) + evaluate(tree.rightChild)
    if tree.symbol == '-':
        return evaluate(tree.leftChild) - evaluate(tree.rightChild)
    if tree.symbol == '*':
        return evaluate(tree.leftChild) * evaluate(tree.rightChild)
    if tree.symbol == '/':
        return evaluate(tree.leftChild) / evaluate(tree.rightChild)

error = False
next_token = '%'

def main():
    file_location = input("Please enter the location of input.txt : ")
    global error, next_token, input_file
    input_file = open(file_location, "r")
    next_token = '$'
    theTree = G()
    input_file.close()
    if not error:
        printTree(theTree)
        value = evaluate(theTree)
        print("The value is", value)
    else:
        print("Input not parsed correctly")

if __name__ == "__main__":
    main()
