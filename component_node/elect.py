class Message:
    def __init__(self, id_elect, port_elect):
        self.id_elect = id_elect
        self.port_elect = port_elect
        self.type = "ELECT"