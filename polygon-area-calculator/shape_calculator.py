class Rectangle:

  def __init__(self, width, height) -> None:
    self.width = width
    self.height = height

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def set_width(self, w):
    self.width = w

  def set_height(self, h):
    self.height = h

  def get_area(self):
    return self.width * self.height

  def get_diagonal(self):
    return (self.width**2 + self.height**2)**0.5

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_picture(self):
    pic = ""
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    for row in range(self.height):
      pic += "*" * self.width + "\n"
    return pic

  def get_amount_inside(self, inshape):
    return (self.width // inshape.width) * (self.height // inshape.height)


class Square(Rectangle):

  def __init__(self, side):
    super().__init__(side, side)

  def __str__(self):
    return f"Square(side={self.width})"

  def set_side(self, side):
    self.width = side
    self.height = side
