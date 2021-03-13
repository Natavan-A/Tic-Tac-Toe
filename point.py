class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

        self.__assignee = None
        
    def set_asignee(self, player):
        self.__assignee = player

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def is_assigned(self):
        return self.__assignee != None