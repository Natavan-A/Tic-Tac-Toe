import requests


class Connection:

    def __init__(self, api_key, user_id):
        self.__url      = 'https://www.notexponential.com/aip2pgaming/api/index.php'
        self.__headers  = { 
                    'User-Agent'   :  'Terminal',
                    'Accept'       :  '*/*',
                    'x-api-key'    :  api_key, 
                    'userId'       :  user_id,
                    'Content-Type' : 'application/x-www-form-urlencoded', 
                }

    def __send_post_request(self, payload):
        return requests.post(self.__url, headers=self.__headers, data=payload)

    def __send_get_request(self, payload):
        return requests.get(self.__url, headers=self.__headers, data=payload)


    def create_a_team(self, name):
        payload = {
            'type': 'team', 
            'name': name
        }

        return self.__send_post_request(payload)

    def create_a_game(self, teamId1, teamId2, gameType='TTT', boardSize=12, target=6):
        payload = {
            'type': 'game', 
            'teamId1': teamId1, 
            'teamId2': teamId2, 
            'gameType': gameType, 
            'boardSize': str(boardSize), 
            'target': str(target)
            }

        return self.__send_post_request(payload)


    def make_a_move(self, move, teamId, gameId):
        payload = { 'type':'move', 'teamId':teamId, 'gameId':gameId, 'move':move }
        return self.__send_post_request(payload)


    def get_my_games(self, open=False):
        payload = 'type=' +'myOpenGames' if open else 'myGames'
        return self.__send_get_request(payload)

    def get_the_move_list(self, gameId, count):
        payload = f'type=moves&gameId={gameId}&count={count}'

        return self.__send_get_request(payload)


    def get_board_string(self, gameId):
        payload = f'type=boardString&gameId={gameId}'

        return self.__send_get_request(payload)

    def get_board_map(self, gameId):
        payload = f'type=boardMap&gameId={gameId}'
        
        return self.__send_get_request(payload)