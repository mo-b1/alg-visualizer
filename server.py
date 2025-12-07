import socket
from _thread import start_new_thread
import pygame
import pickle

class server:
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 64430
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.clock = pygame.time.Clock()
        self.matrix = []


        try:
            self.s.bind((self.ip,self.port))
        except:
            print("socket not binded, most likely port error")

    def accept_new_connections(self):
        self.s.listen()
        i=0
        while True:
            conn,addr = self.s.accept()
            start_new_thread(self.threaded_client, (conn,i))
            i+=1

    def threaded_client(self, conn, id):
        conn.send(pickle.dumps(self.matrix))
        while True:
            self.clock.tick(60)

            matrix = pickle.loads(conn.recv(4096))
            self.matrix = matrix
            conn.send(pickle.dumps(self.matrix))




