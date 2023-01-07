#TOUBAL ZINE-EDDINE SID GROUPE3
#BENALI MOHAMMED YACINE SID GROUPE3
from lib import *

class Part_Out(threading.Thread):
    def __init__(self, elect):
        threading.Thread.__init__(self)
        #initialisation du port voisin
        self.port_next_neighbor = 0
        #initialisation du elect du noeud
        self.elect = elect
        #creation du socket
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #creation d'une instance de event 'afin de gère les conflits'
        self.__flag = threading.Event()
        #on bloque le thread avec la fonction clear()
        self.__flag.clear()

    def run(self):
        try:
            # se connecter au socket du noeud suivant avec 'le port du noeud suivant'
            self.s.connect(("localhost", self.port_next_neighbor))
        except Exception as e:
            print("la partie OUT n'arrive pas a se connecter voisin")
            print(e)
            sys.exit()

        while True:
            #blocage du thread jusqu'à qu'il devient True
            self.__flag.wait()
            #getIDElectSelected() nous permes d'avoir ID du noeud sélectionne après élection
            self.s.send(str(self.elect.getIdElectSelected()).encode())
            print("ID du leader temporaire a été envoyé")
            # getPortElectSelected() nous permes d'avoir PORT du noeud sélectionne après élection
            self.s.send(str(self.elect.getPortElectSelected()).encode())
            print("PORT du leader temporaire a été envoyé")
            self.s.send(b"TOKEN")
            print("TOKEN a été envoyé")
            self.__flag.clear()

    #Mettre le thread en True pour le débloquer
    def resume(self):
        self.__flag.set()
