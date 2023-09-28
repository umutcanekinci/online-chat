import socket
from settings import *
import threading

class Client:

    def __init__(self, playerName):

        self.playerName = playerName

    def Start(self):

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.ConnectToServer()
        
    def ConnectToServer(self):

        self.client.connect(ADDR)
        self.connected = True

        print("[CLIENT] => Connected to server.")
        self.SendMessage(PLAYER_NAME_COMMAND + " " + playerName)

        self.recieveThread = threading.Thread(target=self.RecieveMessage)
        self.recieveThread.start()

        self.sendThred = threading.Thread(target=self.TypeMessage)
        self.sendThred.start()

    def TypeMessage(self):

        while self.connected:

            message = input()

            if message == DISCONNECT_COMMAND:

                self.SendMessage(DISCONNECT_COMMAND)
                self.connected = False
                
            else:
                
                self.SendMessage(MESSAGE_COMMAND + " " + message)
                
    def RecieveMessage(self):

        while self.connected:

            message = self.client.recv(HEADER).decode(FORMAT)
            print(message)

    def SendMessage(self, msg):

        message = msg.encode(FORMAT)

        msgLength = len(message)
        sendLength = str(msgLength).encode(FORMAT)
        sendLength += b' ' * (HEADER - len(sendLength))

        self.client.send(sendLength)
        self.client.send(message)

playerName = input("Enter your nickname => ")
client = Client(playerName)
client.Start()