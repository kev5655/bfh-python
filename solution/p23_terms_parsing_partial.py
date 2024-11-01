# importation of abc module for abstract base classes
from abc import ABCMeta, abstractmethod
# for enum support
from enum import Enum, unique

"""
Parse an arithmetic expression (string) composed of constants, binary operators, and parenthesis only.
(no precedence between the operators. Example:  ((((3+5)-3)*(4+4))/(2*4)) )

This version simply parse an expression and prints all the read tokens.
"""

class ParsingException(Exception):
    """Exception raised if error are discovered during parsing"""

    def __init__(self, message: str) -> None:
        self.message = message


@unique
class Token(Enum):
    "Enumeration of the various tokens in an arithmetic expression"
    CTE  = 0   # constant 0,1,2,...,9
    ADD  = 1   # binary operators
    SUB  = 2
    MUL  = 3
    DIV  = 4
    PARL = 5   # left parenthesis
    PARR = 6   # right parenthesis
    ERR  = 7   # something else -> error
    END  = 8   # all token have been read


class Parser:
    """
    Parser of arithmetic expressions defined by the following grammar (for the sake of simplicity):

       expression := constant
                   | ( expression )
                   | ( expression operator expression )
         operator := + - * /
         constant := 0 | 1 | 2 | ... | 8 | 9

    examples of arithmetic expresssions:
       ((2+(4*5))-(9/3))
       (2*5)
       ((2*5))
       (4)
       7
    """

    def __init__(self, expr: str) -> None:
        """
        Initialises the expression to parse.
        :param: expr: the expression to parse
        """
        self.expr = expr
        self.length = len(self.expr)
        self.idx = 0  # index used by next_token()
        self.current = self.next_token() # reads first token

    def next_token(self) -> Tuple[Token, float]:
        """
        Determines the next token in the expression and returns a tuple composed of the
           [0] the token itself (enum)
           [1] the value (float) used only in case of constant
        :return: tuple with the read token and a value if token is a constant
        """
        if self.idx == self.length: return (Token.END, 0)      # everything has been read, value not used (=0)
        if   self.expr[self.idx] == '0': res = (Token.CTE, 0)  # constant
        elif self.expr[self.idx] == '1': res = (Token.CTE, 1)
        elif self.expr[self.idx] == '2': res = (Token.CTE, 2)


        # ADD YOU CODE HERE


        else: return (Token.ERR,0)                              # something else -> error
        self.idx += 1                                           # increment idx for next time
        return res

    def parse(self) -> None:
        """
        Recursive function to parse an arithmetic expression.
        This version simply prints the tokens.
        """
        if self.current[0] == Token.CTE:                        # constant ?
            print(self.current[1])                              # print the value of constant token
            self.current = self.next_token()                    # reads next token
            return                                              # recursion end
        elif self.current[0] == Token.PARL:                     # ( ?

             
        # ADD YOU CODE HERE

def main() -> None:
    """ Launcher """

    #expr = "4"
    #expr = "((4)+5)"
    #expr = "((4)+(5))"
    #expr = "(((3)+(5))*(4))"
    #expr = "(((8/9)+1)*((7*8)))"
    expr = "((((3+5)-3)*(4+4))/(2*4))"
    #expr = "((4+5+6))"                  # wrong not possible see the grammar
    #expr = "(((3)+(5))*(4))"            # wrong parenthesis not well balanced
    parser = Parser(expr)

    print("Expression:", expr, "\n")

    try:

        # ADD YOU CODE HERE

    except (ParsingException) as error:
        print(error.message)


if __name__ == "__main__":
    main()
