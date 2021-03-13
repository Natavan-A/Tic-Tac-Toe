from point import Point


class Board:
    def __init__(self, size):
        self.__size             = size
        self.__elements         = self.__create(size)
        self.__available_points = size**2

    def __create(self, size):
        row = column = size
        return {f'{x},{y}': Point(x,y) for x in range(row) for y in range(column)}

    def set_point(self, x, y, player):
        point = self.__board[f'{x},{y}']
        point.set_assignee(player)
        self.__available_points -= 1

    def get_size(self):
        return self.__size

    def get_point(self, x, y):
        return self.__board[f'{x},{y}']
    
    def is_full(self):
        return self.__available_points == 0