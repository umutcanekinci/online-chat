import socket
import threading
from settings import *

class Server:

    def Start(self):

        self.playerNames = {}
        self.messages = ""

        # Creating a server socket and providing the address family (socket.AF_INET) and type of connection (socket.SOCK_STREAM), i.e. using TCP connection.
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        print("[SERVER] => Server is started.")
        
        self.Bind()

    def Bind(self):

        try:

            # Binding the socket with the IP address and Port Number.
            self.server.bind(ADDR)

        except socket.error as error:

            print("[SERVER] => An error occured during connecting to server: " + error)

        else:

            print("[SERVER] => Server is binded.")
            
            self.Listen()
        
    def Listen(self):

        self.server.listen()
        print(f"[SERVER] => Server is listening on IP = {IP} at PORT = {PORT}")

        # running an infinite loop to accept continuous client requests.
        while True:

            # Making the server listen to new connections. when a new connection has detected codes will continue 
            clientSocket, addr = self.server.accept()
            print(f"[SERVER] => {addr[0]} is connected.")

            # starting a new thread
            thread = threading.Thread(target=self.HandleClient, args=(clientSocket, addr))
            thread.start()

    def RecieveMessage(self, clientSocket):

        try:

            msgLength = clientSocket.recv(HEADER).decode(FORMAT)

            if not msgLength:
                
                return False

            msgLength = int(msgLength)
            msg = clientSocket.recv(msgLength).decode(FORMAT)
            
            if not ' ' in msg:
                
                return {'command' : msg}

            command, data = msg.split(' ', 1)
            return {'command' : command, 'data' : data}
                
        
        except:

            return False

    def SendMessage(self, clientSockets, message: str):

        for clientSocket in clientSockets:

            clientSocket.send(message.encode(FORMAT))

    def SendMessageToAllClients(self, message):

        self.SendMessage(self.playerNames.keys(), message)

    def HandleClient(self, clientSocket: socket.socket, addr):

        ip, port = addr

        connected = True
        while connected:
            
            message = self.RecieveMessage(clientSocket)

            if message:

                if  message['command'] == PLAYER_NAME_COMMAND:

                    self.playerNames[clientSocket] = message['data']

                    #printing player count and playr name
                    print(f"[SERVER] => {message['data']} ({ip}) is entered to chat from PORT = {port}.")
                    print(f"[SERVER] => Player count is now {str(len(self.playerNames))}.")

                    self.SendMessageToAllClients(f"[SERVER] => {message['data']} is entered to chat.\n")
                    self.SendMessageToAllClients(f"[SERVER] => Player count is now {str(len(self.playerNames))}.")

                elif message['command'] == MESSAGE_COMMAND:
                    
                    self.SendMessageToAllClients(f"[{self.playerNames[clientSocket]}] => {message['data']}")

                elif message['command'] == DISCONNECT_COMMAND:

                    print(f"[SERVER] => {self.playerNames[clientSocket]} ({ip}) is dissconnected.")
                    self.SendMessageToAllClients(f"[SERVER] => {self.playerNames[clientSocket]} has left the chat.")
                    self.playerNames.pop(clientSocket)
                    print(f"[SERVER] => Player count is now {str(len(self.playerNames))}.")
                    connected = False

            else:

                connected = False

        clientSocket.close()

server = Server()
server.Start()