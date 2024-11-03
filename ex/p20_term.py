

from abc import ABC, abstractmethod
from enum import Enum


class Context():

    lookup_table = {}

    def bind(self, name: str, value: float):
        self.lookup_table[name] = value

    def getValue(self, name: str) -> float:
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
