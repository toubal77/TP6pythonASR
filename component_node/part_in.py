#TOUBAL ZINE-EDDINE SID GROUPE3
#BENALI MOHAMMED YACINE SID GROUPE3
from lib import *
from component_node.elect import *


def Handle_Neighbor(con, t, sortie,elect):
    #con: (les donnes) du socket prédécesseur
    #t : 1 s'il a le token, 0 S'il ne possède pas le token
    #elect: objet de la classe Elect
    while True:
        if t==0:
            msgIdElect = con.recv(1024)
            print("ID du leader temporaire est recu")
            msgPortElect = con.recv(1024)
            print("PORT du leader temporaire est recu ")
            msgToken = con.recv(1024)
            print("TOKEN est recu ")
            if msgToken.decode() == "TOKEN":
                print("vous avez recu le token ")
                print("vous avez le droit a la parole")
                print("pour liberer la parole, il faut saisir le mot --TOKEN--")
                data_of_elect_selected = Message(msgIdElect.decode(),msgPortElect.decode())
                #sur_reception_de va nous permettre de faire la comparaison
                elect.sur_reception_de(data_of_elect_selected)
                while True:
                    expression=input("Vous pouvez vous exprimer : ")
                    if expression=="TOKEN":
                        #on vérifie si le noeud reçoit son ID et deja participe a l'election donc c'est le leader
                        if elect.getIdElectSelected() == int(elect.id):
                            #Vérifie s'il a déjà participé à l'élection, si oui alors c'est lui le leader
                            # dans ce cas perce qu'il vient de recevoir son ID
                            if  elect.participe == True:
                                #mettre leader en True
                                elect.leader = True
                                print("le noeud sélectionné après élection est :", int(elect.id))
                                print("FIN DU PROGRAMME")
                            elif elect.participe == False:
                                # mettre participe en True: perce qu'il vas participe a la selection
                                elect.participe = True
                        break
        if t == 1:
            input("Vous etes l'iniateur du token tapez entrer pour le liberer")
        #si il est pas le leader, il libere le noeud suivant, sinon il ne le debloque pas et il le programme s'arrete
        if elect.leader == False:
            #déploquer l'envoie du token pour le noeud suivant
            sortie.resume()
        t = 0




class Part_In(threading.Thread):
    def __init__(self, port, T, S,elect):
        threading.Thread.__init__(self)
        # initialisation du port
        self.port_in = port
        # initialisation du port
        self.t_in = T
        # initialisation du thread sd_out
        self.sortie = S
        # initialisation du elect du noeud
        self.elect = elect
        #creation du socket
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            #attachement du socket avec une adresse IP 'localhost' et le numero du port
            self.ss.bind(('localhost', self.port_in))
        except Exception as e:
            print("Le sd_in n'arrive pas a s'attacher a l'adresse & numero de port")
            print(e)
            sys.exit()
        #socket en mode ecoute passive
        self.ss.listen()

    def run(self):
        #acceptation d'une seul demande de connexion
        self.connexion, self.add = self.ss.accept()
        #appel de la fonction 'handle_heighbor'
        Handle_Neighbor(self.connexion, self.t_in, self.sortie,self.elect)