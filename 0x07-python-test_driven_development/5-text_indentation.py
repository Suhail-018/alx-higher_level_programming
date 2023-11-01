#!/usr/bin/python3
"""
Module: 5-text_indentation

This module defines 'text-indentation' that prints text & with 2-space.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of the characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = [".", "?", ":"]

    lines = []
    line = ""

    for char in text:
        if char in punctuations:
            line += char
            lines.append(line.strip())
            lines.append("")  # Add two new lines
            line = ""
        else:
            line += char

    if line:
        lines.append(line.strip())

    for line in lines:
        print(line)
