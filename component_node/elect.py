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
        #shoould have value of the next noeud
        leader_id = self.id
        leader_port = port_in

    def sur_reception_de(self,M):
        global leader_id, leader_port
        if M.id_elect > leader_id :
            leader_id = M.id_elect
            leader_port = M.port_elect
        else:
            M.id_elect = leader_id
            M.port_elect = leader_port
        self.envoyer_a(M)

    def envoyer_a(self, M):
        M=M
        #bahratli, normalement khasna attribue next_node bsh f projet
        # f les instructions ta3 projet marahach dayratah prof
        # make some research in google
