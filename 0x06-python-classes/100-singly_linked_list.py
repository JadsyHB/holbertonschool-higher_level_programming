#!/usr/bin/python3
"""
Module 100-singly linked list
Node class and SinglyLinkedList class
"""


class Node:
    """
    class Node definition
    Args:
        data
        next_node

    Functions:
        data(self)
        data(self, value)
        next_node(self)
        next_node(self, value)
        __init__(self, data, next_node)
    """

    def __init__(self, data, next_node=None):
        """
        initializes linked list
        Attributes:
            data
            next_node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter
        Returns: data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter

        Args:
            value: sets the data to the value given
        """
        if type(value) is not int:
            raise("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Getter

        Returns: next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter

        Args:
            value: sets the next node to the value given
        """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    class SinglyLinkedList definition

    Args:
        head: private

    Functions:
        __init__(self)
        sorted_insert(self, value)
    """
    def __init__(self):
        """
        initializes singly linked list

        Attributes:
            head: private
        """
        self.__head = None

    def __str__(self):
        """
        print singly linked list each number on line
        """
        string = ""
        cur = self.__head
        while cur is not None:
            string += str(cur.data)
            cur = cur.next_node
            if cur is not None:
                string += "\n"
        return string

    def sorted_insert(self, value):
        """
        Inserts new nodes into singly linked list in sorted order

        Args:
        value: int data for node
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return

        cur = self.__head
        if new.data < cur.data:
            new.next_node = self.__head
            self.__head = new
            return

        while (cur.next_node is not None) and (new.data > cur.next_node.data):
            cur = cur.next_node

        new.next_node = cur.next_node
        cur.next_node = new
        return
