class Move:
    def __init__(self, x, y, assignee=None):
        self.__x = x
        self.__y = y

        self.__assignee = assignee
        self.__related_win_states = []

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_position(self):
        return self.__x, self.__y

    def get_position_str(self):
        return f'{self.__x},{self.__y}'

    def is_assigned(self):
        return self.__assignee != None