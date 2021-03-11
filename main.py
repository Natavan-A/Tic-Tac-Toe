from connection import Connection

if __name__ == "__main__":
    connection = Connection(api_key='c9426ee5181dca77e9a2', user_id='1055')
    
    data, _ = connection.create_a_team(name='helloss')
    print(data)

    #isitend - teamId - 1248
