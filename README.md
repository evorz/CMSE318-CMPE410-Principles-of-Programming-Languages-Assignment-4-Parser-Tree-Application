Write a Python program to parse expressions as
defined by the grammar above, print the abstract syntax tree and compute its value. The
input should be in a file. You should have global variables error (of type Boolean), and
next_token (of type char). Define a function lex() that gets the next character from the file
and places it inside next_token. lex() should skip any white spaces, such as newlines or the
space character. The function unconusmed_input() should return the remaining input in
the file. The last character in the file should always be $. Define functions (hint: class
methods) G(), E(), R(), T(), F() and N(). Inside main(), open the file containing the
expression and call G(). 
