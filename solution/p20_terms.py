# importation of abc module for abstract base classes
from abc import ABC, abstractmethod
# importation of sys module for aborting the program
import sys

"""
This grammar defines terms that can be evaluated using a context to bind values to variables

          Term ::= Constant
                 | Variable
                 | Expression
    Expression ::= Term BinaryOp Term
                 | UnaryOp Term 
"""
class Context:
    """
    Stores the values assigned to the variables into a lookup table (a dictionary).
    Each entry of the lookup table is a pair (name of variable, value)
    Some methods allows us to bind a value to a named variable,
    to change the assignment and to evaluate a variable.
    """

    def __init__(self) -> None:
        """Just create an empty dictionary"""
        self.lookup_table: dict[str, float] = {}

    def bind(self, name: str, value: float) -> None:
        """
        If the variable, called name, does not exist in the dictionary
        lookup_table then a new assignment is added into the dictionary otherwise
        the value of the variable is changed.
        :param name: name of the variable
        :param value: value to assign to the variable
        """
        if not name:  # is name empty
            print("The variable's name is empty")
            sys.exit()
        self.lookup_table[name] = value  # create entry and/or change value

    def get_value(self, name: str) -> float:
        if not name:  # name is empty
            print("The variable's name is empty")
            sys.exit()
        if name in self.lookup_table:
            return self.lookup_table[name]
        else:
            print("The variable '" + name + "' is not bound to a value")
            sys.exit()


class Term(ABC):
    """
    This abstract class defines an abstract method that evaluates
    a term (expression)
    """

    @abstractmethod
    def eval(self, context: Context) -> float:
        """
        Abstract method that evaluate a term.
        :param context: where the bindings (variable name, value) are stored
        :return: the value of the evaluated term
        """
        pass  # no implementation


class Constant(Term):
    """
    The value of a constant cannot (obviously) change.
    The value is initialized during the creation.
    """

    def __init__(self, value: float) -> None:
        """
        Defines the constant value.
        :param value: the constant value to initialize
        """
        self.value = value

    def eval(self, context: Context) -> float:
        """
        :param context: dictionary of bindings (not used in this class but necessary
        :return: simply the value
        """
        return self.value


class Variable(Term):
    """
    The value of a variable can be modified via the context object.
    """

    def __init__(self, name: str) -> None:
        """
        A variable is created and added to the context
        :param name: name of the variable
        """
        self.name = name

    def eval(self, context: Context) -> float:
        """
        :param context: where the bindings (variable name, value) are stored
        :return: the value of the variable
        """
        return context.get_value(self.name)


class BinaryExpression(Term):
    """
    A binary expression has two terms (left, right) and a binary operator.
    """

    def __init__(self, left: Term, right: Term, bin_op: str) -> None:
        """
        :param left: left term
        :param right: right term
        :param bin_op: binary operator (string, "+", "-", "*", "/", etc.)
        """
        self.left = left
        self.right = right
        self.bin_op = bin_op

    def eval(self, context: Context) -> float:
        """
        Evaluates both the terms first and then apply the binary_operator
        :param context: where the bindings (variable name, value) are stored
        :return: the evaluated value of the binary expression
        """
        value_left  = self.left.eval(context)
        value_right = self.right.eval(context)
        bin_op_dict = {
            "+": lambda l, r : l + r,
            "-": lambda l, r : l - r,
            "*": lambda l, r : l * r,
            "/": lambda l, r : l / r
        }
        operation = bin_op_dict[self.bin_op]
        return operation(value_left, value_right)

    def eval2(self, context: Context) -> float:
        """
        Evaluates both the terms first and then apply the binary_operator
        :param context: where the bindings (variable name, value) are stored
        :return: the evaluated value of the binary expression
        """
        value_left = self.left.eval(context)
        value_right = self.right.eval(context)
        match self.bin_op:
            case "+":
                result = value_left + value_right
            case "-":
                result = value_left - value_right
            case "*":
                result = value_left * value_right
            case "/":
                result = value_left / value_right
            case _:
                print("Invalid operator")
                sys.exit()
        return result


class UnaryExpression(Term):
    """
    A unary expression has on term and a unary operator.
    """

    def __init__(self, term: Term, una_op: str) -> None:
        """
        :param term: single term
        :param una_op: binary operator (enum)
        """
        self.term = term
        self.una_op = una_op

    def eval(self, context: Context) -> float:
        """
        Evaluates both the terms first and then apply the binary_operator
        :param context: where the bindings (variable name, value) are stored
        :return: the evaluated value of the binary expression
        """
        value_term = self.term.eval(context)
        una_op_dict = { "-": lambda t: (-1) * t }
        operation = una_op_dict[self.una_op]
        return operation(value_term)


def main() -> None:
    """
    Launcher
    Creates various terms/expressions and evaluate them.
    Finally, the expression (3 + (-d)) * 5) is built and evaluated.
    """
    ctx = Context()
    three = Constant(3)
    five = Constant(5)
    print("Constant 3: ", three.eval(ctx))
    print("Constant 5: ", five.eval(ctx))
    v = Variable("d")
    ctx.bind("d", 7)  # define d = 7
    print("Variable d: ", v.eval(ctx))
    neg = UnaryExpression(v, "-")
    print("-d: ", neg.eval(ctx))
    addition = BinaryExpression(three, neg, "+")
    print("(3 + -d): ", addition.eval(ctx))
    multiplication = BinaryExpression(addition, five, "*")
    print("((3 + -d) * 5): ", multiplication.eval(ctx))


if __name__ == "__main__":
    main()
