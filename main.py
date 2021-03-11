from connection import Connection

if __name__ == "__main__":
    connection = Connection(api_key='c9426ee5181dca77e9a2', user_id='1055')
    
    # data, _ = connection.create_a_team(name='helloss')

    # ADDING TEAM MEMBERS TO TEAMS
    # data, _ = connection.add_a_member(1248, 1055)
    # print(data)
    # data, _ = connection.add_a_member(1248, 1040)
    # print(data)
    # data, _ = connection.add_a_member(1256, 1051)
    # print(data)
    # data, _ = connection.add_a_member(1256, 1040)
    # print(data)
    # data, _ = connection.add_a_member(1256, 1055)
    # print(data)
    
    # CREATING A GAME
    # data, _ = connection.create_a_game(1248, 1256)

    # MAKING A MOVE
    # data, _ = connection.make_a_move(1248, 1474, "4,4")
    # print(data)

    # # MAKING AN OPPONENT MOVE
    # data, _ = connection.make_a_move(1256, 1474, "4,6")
    # print(data)

    data, _ = connection.get_the_move_list(1474)
    moves = data['moves'][0]
    print(moves['teamId'])


    #isitend - teamId - 1248
    #helloss - teamId - 1256
    # 1248-1256 -> gameId - 1474

    # natavan -> 1051
    # aydin   -> 1055
    # ilyas   -> 1040
