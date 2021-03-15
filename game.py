from connection import Connection
from board import Board
from team import Team
from move import Move


class Game:
    def __init__(self, api_key, user_id):
        self.__id               = None
        self.__board            = None
        self.__my_team          = None
        self.__opponent_team    = None
        self.__connection       = Connection(api_key=api_key, user_id=user_id)

    def __set_id(self, id):
        self.__id = id

    def set_board(self, size=12, target=6):
        self.__board = Board(size, target)
    
    def set_my_team(self, id, sign):
        self.__my_team = Team(id, sign, self.__board)

    def set_opponent_team(self, id, sign):
        self.__opponent_team = Team(id, sign, self.__board)

    def create(self, game_type="TTT"):
        player_1    = self.__me.get_id() if self.__me.get_sign().lower() == 'x' else self.__opponent.get_id()
        player_2    = self.__me.get_id() if self.__me.get_sign().lower() == 'o' else self.__opponent.get_id()
        board_size  = self.__board.get_size()
        target      = self.__target

        # MAKING API REQUEST
        response    = self.__connection.create_a_game(player_1, player_2, game_type, board_size, target)
        
        # CHECKING WHETHER THE REQUEST IS VALID
        if self.__connection.validate(response):
            game_id = response.json()['gameId']
            self.__id = game_id
            print(f'You created the game: {game_id}')

    def connect(self, game_id, board_size=12, target=6):
        response = self.__connection.get_board_string(game_id)
        if self.__connection.validate(response):
            self.__set_id(game_id)

            print(f'You are connected to the game: {game_id}')


    def play(self):
        if self.__my_team.is_turn:
            x, y = 0, 0 # calculated by minimax, by default I gave x = 0 and y = 0
            response = self.__connection.make_a_move(teamId=self.__my_team.get_id(), gameId=self.__id, move=f'{x},{y}')
            
            if self.__connection.validate(response):
                move = Move(x, y, self.__my_team)
                self.__my_team.played()
        else:
            response = self.__connection.get_the_move_list(gameId=self.__id)

            if self.__connection.validate(response):
                x, y = map(int, response.json()['moves'].split())
                move = Move(x, y, self.__opponent_team)
                self.__opponent_team.played()

        self.__board.set_move(move)



        
        