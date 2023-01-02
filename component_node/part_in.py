from lib import *
import socket

def Handle_Neighbor (con, add, t, sortie):
    while True:
        if t == 0:
            msg = con.recv(1024)
            if msg.decode() == "TOKEN":
                print("vous avez recu le token")
                print("vous avez le droit a la parole")
                print("pour liberer la parole, il faut saisir le mot --TOKEN--")
                while True:
                    expression = input("Vous pouvez vous exprimer : ")
                    if expression == "TOKEN":
                        break
        if t == 1:
            input("Vous etes l'iniateur du token tapez entrer pour le liberer")
        sortie.resume()
        t = 0

class Part_In(threading.Thread):

    def __init__(self,port, T,s):
        threading.Thread.__init__(self)

        self.port_in = port
        self.t_in = T
        self.sortie = s
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        try:
            self.ss.bind(('127.0.0.1', self.port_in))
        except:
            print("le sd_in n'arrive pas a s'attacher a l'adresse & numero de port")
            sys.exit()
        self.msg_in = self.ss.recvfrom(1024)

    def run(self):
        #dans la methode run(), socket accept une seul demande de connexion
        self.connexion, self.add=self.ss.accept()

        #appel de la fonction handle_neighbor qui est defini en haut de ce module
        #part_in.py
        Handle_Neighbor(self.connexion, self.add, self.T, self.sortie)
