class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self):
        pass

    def head(self):
        pass

    def tail(self):
        pass

    def is_empty(self):
        pass

    def insert_node_to_tail(self, node):
        pass

    def insert_node_to_head(self, node):
        pass

    def insert_after(self, previous_node, new_node):
        pass

    def remove_tail(self):
        pass

    def print_list(self):
        pass

    def find(self):
        pass

    def size(self):
        pass

    def reverse(self):
        pass


import unittest


class LinkedListTests(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()

    def test_insert_first_node_to_tail(self):
        pass

    def test_insert_first_node_to_head(self):
        pass

    def test_insert_two_nodes_to_head(self):
        pass

    def test_insert_two_nodes_to_tail(self):
        pass

    def test_insert_nodes_to_head_and_tail(self):
        pass

    def test_is_empty_with_empty_linked_list(self):
        pass

    def test_is_empty_with_two_nodes(self):
        pass

    def test_insert_after_node_to_middle(self):
        pass

    def test_print_list(self):
        pass

    def test_remove_tail(self):
        pass