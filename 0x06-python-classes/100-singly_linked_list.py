#!/usr/bin/python3
"""Module containing the Node and SinglyLinkedList class."""


class Node:
    """The node class designed for queue, singlylinked list, stack."""

    def __init__(self, data, next_node=None):
        """Initialization of the node.
        Args:
            data (int): The integer value to be stored in the node.
            next_node (:obj:'Node'): The next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """int: Integer value stored in the node."""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """:obj:'Node': The next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """The singlylinked list class"""

    def __init__(self):
        """Initialization of the singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a node in increasing order of the singly linked list.
        Args:
            value (int): The integer value of the node to be inserted into the
                singly linked list.
        """
        curr_n = self.__head
        if curr_n is None or value < curr_n.data:
            self.__head = Node(value, curr_n)
        else:
            while (curr_n.next_node is not None and
                    value >= curr_n.next_node.data):
                    curr_n = curr_n.next_node
            curr_n.next_node = Node(value, curr_n.next_node)

    def __str__(self):
        """Returns a string containing the integer values of each node on
        separate lines
        Returns:
            str: The string of integers values
        """
        string = ""
        if self.__head is not None:
            string = str(self.__head.data)
            curr_n = self.__head.next_node
            while curr_n is not None:
                string += "\n"
                string += str(curr_n.data)
                curr_n = curr_n.next_node
        return string
