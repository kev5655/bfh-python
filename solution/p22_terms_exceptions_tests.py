"""
Collection of unit tests for term_exceptions.py
"""

import unittest
from terms_exceptions import *


class TestContext(unittest.TestCase):

    def test_bind_get_value(self):
        """
        Checks that binding an identifier with a float value and get_value return the same value
        assertAlmostEqual(actual, expected, delta) is used instead of assertEqual because of float.
        """
        delta = 1E-6
        identifier = "v"
        value = 10.5
        a_var = Variable(identifier)
        ctx = Context()
        ctx.bind(identifier, value)
        self.assertAlmostEqual(ctx.get_value(identifier), value, delta=delta)

    def test_bind_with_blank_space(self):
        """Checks that binding an identifier with blank space raises an exception"""
        identifier = " x"
        ctx = Context()
        value = 0.0
        with self.assertRaises(WrongNameVariableException):
            ctx.bind(identifier, value)

    def test_bind_not_alphanum(self):
        """Checks that binding an identifier with non alphanum letters raises an exception"""
        identifier = "x="
        ctx = Context()
        value = 0.0
        with self.assertRaises(WrongNameVariableException):
            ctx.bind(identifier, value)

    def test_bind_empty(self):
        """Checks that binding an empty identifier raises an exception"""
        identifier = ""
        ctx = Context()
        value = 0.0
        with self.assertRaises(WrongNameVariableException):
            ctx.bind(identifier, value)

    def test_get_value_with_blank_space(self):
        """Checks that getting a value for an identifier with blank space raises an exception"""
        identifier = "x"
        ctx = Context()
        with self.assertRaises(NotBoundException):
            ctx.get_value(identifier)


class TestConstant(unittest.TestCase):

    def test_eval(self):
        """Checks the evaluation of a constant works fine"""
        value = 4.03
        four = Constant(value)
        ctx  = Context()
        self.assertEqual(Constant.eval(four, ctx), value)


class TestVariable(unittest.TestCase):

    def test_eval(self):
        """Checks that the evaluation of a variable works fine"""
        identifier = "v"
        value = 10.5
        a_var = Variable(identifier)
        ctx = Context()
        ctx.bind(identifier, value)
        self.assertEqual(a_var.eval(ctx), value)

    def test_creation_with_blank_space(self):
        """Checks that the creation of a variable with blank spaces raises an exception"""
        emtpy_identifier = " x"
        with self.assertRaises(WrongNameVariableException):
            a_var = Variable(emtpy_identifier)

    def test_creation_not_alphanum(self):
        """Checks that the creation of a variable with non alphanum letters raises an exception"""
        emtpy_identifier = "x="
        with self.assertRaises(WrongNameVariableException):
            a_var = Variable(emtpy_identifier)

    def test_creation_empty(self):
        """Checks that the creation of an empty variable raises an exception"""
        emtpy_identifier = ""
        with self.assertRaises(WrongNameVariableException):
            a_var = Variable(emtpy_identifier)


class TestBinaryExpression(unittest.TestCase):

    def test_eval(self):
        """Checks that the evaluation of a binary expression works fine for each operator"""
        value = 5.0
        term = Constant(value)
        ctx = Context()
        bin_expr = BinaryExpression(term, term, BinOp.ADD)
        self.assertEqual(bin_expr.eval(ctx), value+value)
        bin_expr = BinaryExpression(term, term, BinOp.SUB)
        self.assertEqual(bin_expr.eval(ctx), value-value)
        bin_expr = BinaryExpression(term, term, BinOp.MUL)
        self.assertEqual(bin_expr.eval(ctx), value*value)
        value2 = 2.0
        term_right = Constant(value2)
        bin_expr = BinaryExpression(term, term_right, BinOp.DIV)
        self.assertEqual(bin_expr.eval(ctx), value/value2)

    def test_division_by_zero(self):
        ctx = Context()
        five = Constant(5.0)
        zero = Constant(0.0)
        bin_expr_division_by_zero = BinaryExpression(five, zero, BinOp.DIV)
        with self.assertRaises(ZeroDivisionError):
            bin_expr_division_by_zero.eval(ctx)


class TestUnaryExpression(unittest.TestCase):

    def test_eval(self):
        """Checks that the evaluation of a unary expression works fine"""
        value = 5.0
        term = Constant(value)
        ctx = Context()
        una_expr = UnaryExpression(term, UnaOp.NEG)
        self.assertEqual(una_expr.eval(ctx), (-1) * value)


if __name__ == '__main__':
    unittest.main()
