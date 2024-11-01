# importation of abc module for abstract base classes
from abc import ABC, abstractmethod
# for enum support
from enum import Enum, unique, auto
# for override decorator (from Python 3.12)
from typing_extensions import override

"""
This grammar defines terms that can be evaluated using a context to bind values to variables

          Term ::= Constant
                 | Variable
                 | Expression
    Expression ::= Term BinaryOp Term
                 | UnaryOp Term 
"""

def is_not_valid(name: str) -> bool:
    """
    A variable name must follow the rules:
    1. cannot be empty
    2. cannot be blank
    3. cannot contain blank spaces
    4. must be composed of alphanumeric letters only

    :param name: name to check the rules
    :return: true if the name is invalid, false otherwise
    """
    return name == "" or name.isspace() or not name.isalnum()


@unique
class BinOp(Enum):
    """Enumeration of all supported binary operators"""
    ADD = auto()
    SUB = auto()
    MUL = auto()
    DIV = auto()


@unique
class UnaOp(Enum):
    """Enumeration of all supported unary operators"""
    NEG = auto()


class WrongNameVariableException(Exception):
    """
    Raised whenever a variable name is not valid.
    """

    def __init__(self, name: str, message="The following variable name does not follow the rules: ") -> None:
        """
        :param name: name of the variable involved in the exception
        :param message: the message of the exception
        """
        self.name = name
        self.message = message
        super().__init__(self.message)

    @override
    def __str__(self):
        return self.message + f"'{self.name}'"


class NotBoundException(Exception):
    """Raised whenever a variable is not bound with a value in a context."""

    def __init__(self, name: str, message = "The following variable name is not bound: ") -> None:
        self.name = name
        self.message = message
        super().__init__(self.message)

    @override
    def __str__(self):
        return self.message + f"'{self.name}'"


class Context:
    """
    Stores the values assigned to the variables into a lookup table (a dictionary).
    Each entry of the lookup table is a pair (name of variable, value)
    Some methods allows us to bind a value to a named variable,
    to change the assignment and to evaluate a variable.
    """

    def __init__(self) -> None:
        """ Create an empty dictionary. """
        self.lookup_table: dict[str, float] = {}

    def bind(self, name: str, value: float) -> None:
        """
        If the variable name does not exist in the dictionary lookup_table,
        a new assigment is added into the dictionary otherwise
        the value of the variable is changed.
        :param name: name of the variable
        :param value: value to assign to the variable
        :raises EmptyBlankException: if the variable is empty of blank
        :raises NotBoundException: if the variable is not bound with a value in a context
        """
        if is_not_valid(name):  # is name empty or blank
            raise WrongNameVariableException(name)
        self.lookup_table[name] = value  # create entry and/or change value

    def get_value(self, name: str) -> float:
        """
        Find in the context the entry [name, value] and return value
        :param name: name of the variable
        :return: the value bound to the variable name
        :raises NotBoundException: if the variable is not bound with a value in a context
        :raises EmptyBlankException: if the variable name is not valid
        """
        if is_not_valid(name):  # name is empty or blank
            raise WrongNameVariableException(name)
        if not name in self.lookup_table:
            raise NotBoundException(name)
        else:
            return self.lookup_table[name]


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
        Defines the value of a constant.
        :param value: the value of the constant
        """
        self.value = value

    @override
    def eval(self, context: Context) -> float:
        """
        :param context: where the bindings (variable name, value) are stored, not used but necessary (c.f. Term)
        :return: simply the value
        """
        return self.value


class Variable(Term):
    """
    A variable is composed of a name only. The value of a variable can be modified via the context object.
    """

    def __init__(self, name: str) -> None:
        """
        A variable is created and added to the context
        :param name: name of the variable
        :raises WrongNameException: if the variable name is invalid
        """
        if is_not_valid(name):  # is name invalid
            raise WrongNameVariableException(name)
        self.name = name

    @override
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

    def __init__(self, left: Term, right: Term, bin_op: BinOp) -> None:
        """
        :param left: left term
        :param right: right term
        :param bin_op: binary operator (enum)
        """
        self.left = left
        self.right = right
        self.bin_op = bin_op

    @override
    def eval(self, context: Context) -> float:
        """
        Evaluates both the terms first and then apply the binary_operator
        :param context: where the bindings (variable name, value) are stored
        :return: the evaluated value of the binary expression
        """
        value_left = self.left.eval(context)
        value_right = self.right.eval(context)
        bin_op_dict = {
            BinOp.ADD: lambda l, r: l + r,
            BinOp.SUB: lambda l, r: l - r,
            BinOp.MUL: lambda l, r: l * r,
            BinOp.DIV: lambda l, r: l / r
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
            case BinOp.ADD:
                result = value_left + value_right
            case BinOp.SUB:
                result = value_left - value_right
            case BinOp.MUL:
                result = value_left * value_right
            case BinOp.DIV:
                result = value_left / value_right
        return result


class UnaryExpression(Term):
    """
    A unary expression has a single term and a unary operator.
    """

    def __init__(self, term: Term, una_op: UnaOp) -> None:
        """
        :param term: single term
        :param una_op: binary operator (enum)
        """
        self.term = term
        self.una_op = una_op

    @override
    def eval(self, context: Context) -> float:
        """
        Evaluates both the terms first and then apply the binary_operator
        :param context: where the bindings (variable name, value) are stored
        :return: the evaluated value of the binary expression
        """
        value_term = self.term.eval(context)
        una_op_dict = { UnaOp.NEG: lambda t: (-1) * t }
        operation = una_op_dict[self.una_op]
        return operation(value_term)


def main() -> None:
    """ Launcher """
    ctx = Context()
    three = Constant(3)
    five = Constant(5)
    print("Constant 3: ", three.eval(ctx))
    print("Constant 5: ", five.eval(ctx))
    try:
        v: Variable = Variable("d")
    except WrongNameVariableException as e:
        print(e)

    ctx.bind("d", 7)  # define d = 7
    try:
        print("Variable d: ", v.eval(ctx))
    except (WrongNameVariableException, NotBoundException) as e:
        print(e)

    neg = UnaryExpression(v, UnaOp.NEG)
    print("-d: ", neg.eval(ctx))
    addition = BinaryExpression(three, neg, BinOp.ADD)
    print("(3 + (-d)): ", addition.eval(ctx))
    multiplication = BinaryExpression(addition, five, BinOp.MUL)
    print("((3 + -d) * 5): ", multiplication.eval(ctx))

    try:
        v2 = Variable("v2")
        print("Variable v2: ", v2.eval(ctx))
    except (WrongNameVariableException, NotBoundException) as e:
        print(e)

    try:
        v3 = Variable("")
        print("Variable v3: ", v3.eval(ctx))
    except (WrongNameVariableException, NotBoundException) as e:
        print(e)

if __name__ == "__main__":
    main()
