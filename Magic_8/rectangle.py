class Rectangle(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    '''In the future, if I continue this it might be helpful to create a
    coordinate class.'''
    def in_rect(self, x, y):
        if x >= self.x and x <= (self.x + self.width):
            if y >= self.y and y <= self.y + self.height:
                return True
            else:
                return False
        else:
            return False
