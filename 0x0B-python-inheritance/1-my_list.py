#!/usr/bin/python3
"""
my list module
"""


class MyList(list):
    """
    inherited from list instance
    print sorted 
    """
    def print_sorted(self):
        """
        prints the sorted list
        """
        print(sorted(self))
