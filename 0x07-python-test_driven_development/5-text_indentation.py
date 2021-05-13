#!/usr/bin/python3
"""
Module 5-text_indentation
"""



def text_indentation(text):
    """
    prints a text with 2 new lines after ? : . characters
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        for char in ".?:":
            text = text.replace(char, char +"\n\n")
        list_text = [line.strip(' ') for line in text.split('\n')]
        new_text = "\n".join(list_text)
        print(new_text, end="")
