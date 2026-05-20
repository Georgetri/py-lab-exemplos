class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None


    def head(self):
        return self._head


    def tail(self):
        return self._tail


    def is_empty(self):
        return self._head is None


    def insert_node_to_head(self, node):
        if self.is_empty():
            self._head = node
            self._tail = node
        else:
            node.next = self._head
            self._head = node


    def insert_node_to_tail(self, node):
        if self.is_empty():
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            self._tail = node


    def remove_head(self):
        if self.is_empty():
            return None
        else:
            node_removed = self._head
            self._head = self._head.next

        if self._head is None:
            self._tail = None

        node_removed.next = None
        return node_removed


    def print_list(self):
        current = self._head
        result = ''

        while current is not None:
            result += current.value + '->'
            current = current.next

        result += 'None'
        return result



    def insert_after(self,previous_node:Node, new_node:Node):
        new_node.next = previous_node.next
        previous_node.next = new_node

        if previous_node == self._tail:
            self._tail = new_node


    def remove_tail(self):
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
        self.linked_list.insert_node_to_tail(Node('tail'))
        self.assertEqual('tail', self.linked_list.tail().value)


    def test_insert_first_node_to_head(self):
        self.linked_list.insert_node_to_head(Node('head'))
        self.assertEqual('head', self.linked_list.head().value)


    def test_insert_two_nodes_to_head(self):
        self.linked_list.insert_node_to_head(Node('head2'))
        self.linked_list.insert_node_to_head(Node('head1'))
        self.assertEqual('head1', self.linked_list.head().value)


    def test_insert_two_nodes_to_tail(self):
        self.linked_list.insert_node_to_tail(Node('tail2'))
        self.linked_list.insert_node_to_tail(Node('tail1'))
        self.assertEqual('tail1', self.linked_list.tail().value)


    def test_insert_nodes_to_head_and_tail(self):
        self.linked_list.insert_node_to_head(Node('head'))
        self.linked_list.insert_node_to_tail(Node('tail'))

        self.assertEqual('head', self.linked_list.head().value)
        self.assertEqual('tail', self.linked_list.tail().value)


    def test_is_empty_with_empty_linked_list(self):
        self.assertTrue(self.linked_list.is_empty())


    def test_is_empty_with_two_nodes(self):
        self.linked_list.insert_node_to_head(Node('element'))
        self.linked_list.insert_node_to_head(Node('element2'))

        self.assertFalse(self.linked_list.is_empty())


    def test_insert_after_middle_node(self):

        node_head = Node('A')
        node_tail = Node('C')
        node_after = Node('B')
        self.linked_list.insert_node_to_head(node_head)
        self.linked_list.insert_node_to_tail(node_tail)
        self.linked_list.insert_after(node_head,node_after)

        self.linked_list.insert_after(node_after, Node('X'))
        self.assertEqual('X', self.linked_list.head().next.next.value)
        self.assertEqual('C', self.linked_list.tail().value)


    def test_print_list(self):
        node_head = Node('head')

        self.linked_list.insert_node_to_head(node_head)
        self.linked_list.insert_after(node_head,Node('middle'))
        self.linked_list.insert_node_to_tail(Node('tail'))
        self.assertEqual('head->middle->tail->None',self.linked_list.print_list())

        print(self.linked_list.print_list())



if __name__=='__main__':
    unittest.main()
