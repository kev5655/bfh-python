

from enum import Enum
from abc import ABC, abstractmethod
from typing import override


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

    def __init__(self, name: str, message="The following variable name is not bound: ") -> None:
        self.name = name
        self.message = message
        super().__init__(self.message)

    @override
    def __str__(self):
        return self.message + f"'{self.name}'"


def is_not_valid(name: str) -> bool:
    return name == "" or name.isspace() or not name.isalnum()


class Context():

    lookup_table = {}

    def bind(self, name: str, value: float):
        if is_not_valid(name):
            raise WrongNameVariableException(name)
        self.lookup_table[name] = value

    def getValue(self, name: str) -> float:
        if is_not_valid(name):
            raise WrongNameVariableException(name)
        if not name in self.lookup_table:
            raise NotBoundException(name)
        return self.lookup_table[name]


class Term(ABC):

    @abstractmethod
    def eval(context: Context) -> float:
        pass


class Constant(Term):
    def __init__(self, value: float):
        self.value = value

    def eval(self, context: Context) -> float:
        return self.value


class Variable(Term):
    def __init__(self, name: str):
        if is_not_valid(name):
            raise WrongNameVariableException(name)
        self.name = name

    def eval(self, context: Context) -> float:
        return context.getValue(self.name)


class BinaryExpression(Term):
    def __init__(self, left: Term, right: Term, operator: str):
        self.operator = validate_operator(operator)
        self.left = left
        self.right = right

    def eval(self, context: Context) -> float:
        match self.operator:
            case Operator.ADD:
                return self.left.eval(context) + self.right.eval(context)
            case Operator.SUB:
                return self.left.eval(context) - self.right.eval(context)
            case Operator.MUL:
                return self.left.eval(context) * self.right.eval(context)
            case Operator.DIV:
                return self.left.eval(context) / self.right.eval(context)


class UnaryExpression(Term):
    def __init__(self, term: Term, operator: str):
        self.operator = validate_unary_operator(operator)
        self.term = term

    def eval(self, context: Context) -> float:
        match self.operator:
            case UnaryOperator.INC:
                return self.term.eval(context) + 1
            case UnaryOperator.DEC:
                return self.term.eval(context) - 1
            case UnaryOperator.PLU:
                return self.term.eval(context) * +1
            case UnaryOperator.MIN:
                return self.term.eval(context) * -1


class Operator(Enum):
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"


class UnaryOperator(Enum):
    INC = "++"
    DEC = "--"
    PLU = "+"
    MIN = "-"


def validate_operator(operator: str) -> Operator:
    match(operator):
        case Operator.ADD.value:
            return Operator.ADD
        case Operator.SUB.value:
            return Operator.SUB
        case Operator.MUL.value:
            return Operator.MUL
        case Operator.DIV.value:
            return Operator.DIV
        case _:
            raise ("Operator is not valid")


def validate_unary_operator(operator: str) -> UnaryOperator:
    match(operator):
        case UnaryOperator.INC.value:
            return UnaryOperator.INC
        case UnaryOperator.DEC.value:
            return UnaryOperator.DEC
        case UnaryOperator.PLU.value:
            return UnaryOperator.PLU
        case UnaryOperator.MIN.value:
            return UnaryOperator.MIN
        case _:
            raise ("Unary Operator is not valid")


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

    neg = UnaryExpression(v, UnaryOperator.MIN)
    print("-d: ", neg.eval(ctx))
    addition = BinaryExpression(three, neg, Operator.ADD)
    print("(3 + (-d)): ", addition.eval(ctx))
    multiplication = BinaryExpression(addition, five, Operator.MUL)
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