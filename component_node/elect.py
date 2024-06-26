#TOUBAL ZINE-EDDINE SID GROUPE3
#BENALI MOHAMMED YACINE SID GROUPE3
from uuid import uuid4

leader_id = 0
leader_port = 0

class Message:
    def __init__(self, id_elect, port_elect):
        self.id_elect = id_elect
        self.port_elect = port_elect
        self.type = "ELECT"

class Elect:
    def __init__(self, port_in):
        global leader_port, leader_id
        self.id = uuid4()
        self.port = port_in
        self.leader = False
        self.participe = False
        leader_id = self.id
        leader_port = port_in

    #remarque: la fonction uuid qui genere un ID unique return un ID de 128 bit
    # on converte 128 bit value en valeur INT afin de pouvoir la compare


    #fonction getter: pour avoir ID de leader
    def getIdElectSelected(self):
        return int(leader_id)

    # fonction getter: pour avoir PORT de leader
    def getPortElectSelected(self):
        return int(leader_port)

    def sur_reception_de(self, M):
        #on converti M.id_elect et leader_id en INT car on les a recu en bytes chaine de caractere.decode()
        #donc on les converti en INT pour pouvoir les comparer
        global leader_id, leader_port
        print("la comparaison vas etre entre %d et %d"%(int(M.id_elect),int(leader_id)))
        if int(M.id_elect) > int(leader_id):
            leader_id = int(M.id_elect)
            leader_port = int(M.port_elect)
            print("le noeud selectionne apres comparaison est %d" % (leader_id))
        else:
            M.id_elect = int(leader_id)
            M.port_elect = int(leader_port)
            print("le noeud selectionne apres comparaison est %d" % (int(M.id_elect)))

