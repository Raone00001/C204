
import socket
from  threading import Thread

SERVER = None
PORT = None
IP_ADDRESS = None

# dictionary where they will accept the player #
CLIENTS = {}

# earler, created databases (firbase) and stored info for players for multiplayer games
# here, using socket fromn python and building connection with server and client and sending info without databases

# server accepting client info
def acceptConnections():
    # creating global vars to connect
    global CLIENTS
    global SERVER

    while True:
        # server accepting client info
        player_socket, addr = SERVER.accept()

        player_name = player_socket.recv(1024).decode().strip()

        # storing player info
        if (len(CLIENTS.keys()) == 0):
            
            CLIENTS[player_name] = {'player_type' : 'player1'}
        else:
            CLIENTS[player_name] = {'player_type' : 'player2'}

        CLIENTS[player_name]["player_socket"] = player_socket
        CLIENTS[player_name]["address"] = addr
        CLIENTS[player_name]["player_name"] = player_name
        CLIENTS[player_name]["turn"] = False

        print(f"connection established with {player_name} : {addr}")


def setup():
    print("\n")
    print("\t\t\t\t\t\t*** LUDO LADDER ***")


    global SERVER
    global PORT
    global IP_ADDRESS

    IP_ADDRESS = '127.0.0.1'
    PORT = 5000
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(10)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMMING CONNECTIONS...")
    print("\n")

    acceptConnections()


setup()
