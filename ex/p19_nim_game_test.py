import unittest
from .p19_nim_game import gen_rand_list, is_end


class TestNimGame(unittest.TestCase):

    def test_gen_rand_list(self):
        self.assertEqual(len(gen_rand_list(3)), 3)

    def test_is_end(self):
        empty_stack = [0, 0, 0, 0]
        self.assertEqual(is_end(empty_stack), True)
        stack = [1, 0, 0, 0]
        self.assertEqual(is_end(stack), False)
        stack = [1, 1, 1, 1]
        self.assertEqual(is_end(stack), False)
