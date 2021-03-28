from exceptions import *
import requests
import sys


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

    def __send_get_request(self, params):
        return requests.get(self.__url + '?' + params, headers=self.__headers, data={})

    def create_a_team(self, name):
        payload = {
            'type': 'team', 
            'name': name
        }
        response = self.__send_post_request(payload)
        return self.__validate(response)


    def add_a_member(self, teamId, userId):
        payload = {
            'type'  : 'member', 
            'teamId': teamId,
            'userId': userId
        }
        response = self.__send_post_request(payload)
        return self.__validate(response)


    def create_a_game(self, teamId1, teamId2, gameType, boardSize, target):
        payload = {
            'type'     : 'game', 
            'teamId1'  : teamId1, 
            'teamId2'  : teamId2, 
            'gameType' : gameType, 
            'boardSize': str(boardSize), 
            'target'   : str(target)
        }
        response = self.__send_post_request(payload)
        return self.__validate(response)


    def make_a_move(self, teamId, gameId, move):
        payload = { 
            'type'  : 'move', 
            'teamId': teamId, 
            'gameId': gameId, 
            'move'  : move 
        }
        response = self.__send_post_request(payload)
        return self.__validate(response)


    def get_my_games(self, all=False):
        params      = 'type=' + 'myGames' if open else 'myOpenGames'
        response    = self.__send_get_request(params)
        return self.__validate(response)


    def get_the_move_list(self, gameId, count=1):
        params      = f'type=moves&gameId={gameId}&count={count}'
        response    = self.__send_get_request(params)
        return self.__validate(response)


    def get_board_string(self, gameId):
        params      = f'type=boardString&gameId={gameId}'
        response    = self.__send_get_request(params)
        return self.__validate(response)


    def get_board_map(self, gameId):
        params   = f'type=boardMap&gameId={gameId}'
        response = self.__send_get_request(params)
        return self.__validate(response)

    def __validate(self, response):
        try:
            if not response:
                raise HTTPRequestFailureException

            data = response.json()
            if not data['code'] == 'OK':
                raise APIFailureException
            
            return data

        except HTTPRequestFailureException:
            print(f'Request has failed with {response.status_code} status code.')
            return None
        except APIFailureException:
            print(f'Api returned {data["code"]} code with the below message\n{data["message"]}' if data["message"] else ".")
            return None