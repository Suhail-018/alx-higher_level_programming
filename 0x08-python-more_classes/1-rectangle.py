#!/usr/bin/python3
class Rectangle:
  """
  This class defines a rectangle.

  Attributes:
    width: The width of the rectangle.
    height: The height of the rectangle.

  Methods:
    width: Returns the width of the rectangle.
    height: Returns the height of the rectangle.
    set_width: Sets the width of the rectangle.
    set_height: Sets the height of the rectangle.
  """

  def __init__(self, width=0, height=0):
    """
    Initialize the rectangle.

    Args:
      width: The width of the rectangle.
      height: The height of the rectangle.
    """
    self._width = width
    self._height = height

  @property
  def width(self):
    """
    Return the width of the rectangle.
    """
    return self._width

  @width.setter
  def width(self, value):
    """
    Set the width of the rectangle.

    Args:
      value: The new width of the rectangle.

    Raises:
      TypeError: If value is not an integer.
      ValueError: If value is less than 0.
    """
    if not isinstance(value, int):
      raise TypeError("width must be an integer")
    if value < 0:
      raise ValueError("width must be >= 0")
    self._width = value

  @property
  def height(self):
    """
    Return the height of the rectangle.
    """
    return self._height

  @height.setter
  def height(self, value):
    """
    Set the height of the rectangle.

    Args:
      value: The new height of the rectangle.

    Raises:
      TypeError: If value is not an integer.
      ValueError: If value is less than 0.
    """
    if not isinstance(value, int):
      raise TypeError("height must be an integer")
    if value < 0:
      raise ValueError("height must be >= 0")
    self._height = value
