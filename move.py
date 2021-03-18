class Move:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__value = None
        self.__assignee = None


    def set_value(self, value):
        self.__value = value
    
    def get_value(self):
        return self.__value
        
    def set_assignee(self, player):
        self.__assignee = player

    def revoke_assignee(self, value):
        self.__assignee = None

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_position(self):
        return (self.__x, self.__y)

    def get_assignee(self):
        return self.__assignee

    def is_assigned(self):
        return self.__assignee != None