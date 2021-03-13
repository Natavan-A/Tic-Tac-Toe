class Team:
    def __init__(self, id, sign, target):
        self.__id             = id
        self.__sign           = None
        self.__is_turn        = False
        self.__plays          = []
        self.__goals          = None #self.__find_goal_states(target)


    def add_play(self, play):
        self.__plays.append(play)

    def get_id(self):
        return self.__id

    def get_sign(self):
        return self.__sign

    def get_plays(self):
        return self.__plays

    def is_turn(self):
        return self.__is_turn

    def __find_goal_states(self):
        pass