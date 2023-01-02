import uuid

# za3ma var global
leader_id = uuid.uuid1()
leader_port = 0
class Elect():

    # i'm not sure about that
    # code is made just to see what we do, and after we implement correctly
    def __init__(self,idElect, portElect):
        global leader_port
        self.type = "ELECT"
        self.id_elect = idElect
        self.port_elect = portElect
        leader_port = portElect

    def sur_reception_de(self, M):
        global leader_port, leader_id
        if M.id_elect > leader_id:
            leader_id = M.id_elect
            leader_port = M.port_elect
        else:
            M.id_elect = leader_id
            M.port_elect = leader_port

    def envoyer_a(M):
        # function send message
