class Rectangle:
    def overlaps(self, rect):

        if self.get_left_x() > rect.get_right_x() or self.get_right_x() < rect.get_left_x():
            return False
        elif self.get_top_y() < rect.get_bottom_y() or self.get_bottom_y() > rect.get_top_y():
            return False
        return True

    # don't touch below this line

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"


"""
self.get_left_x() <= rect.get_right_x(): The left edge of this rectangle is at or to the left of the other's right edge.
self.get_right_x() >= rect.get_left_x(): The right edge of this rectangle is at or to the right of the other's left edge.
self.get_top_y() >= rect.get_bottom_y(): The top edge of this rectangle is at or above the other's bottom edge.
self.get_bottom_y() <= rect.get_top_y(): The bottom edge of this rectangle is at or below the other's top edge.
"""
