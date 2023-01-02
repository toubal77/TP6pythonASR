import threading

from lib import  *

class Part_Out(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.__flag = threading.Event()
        self.__flag.clear() # clear() bloque the thread
        #initialiser le port du noeud voisin
        self.port_next_neighbor = 0

        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def run(self):
        try:
            self.s.connect(('127.0.0.1', self.port_next_neighbor))
        except:
            print("la partie OUT n'arrive pas a se connecter voisin")
            sys.exit()
        while True:
            self.__flag.wait()
            self.s.send(b"TOKEN")
            self.__flag.clear()

    def resume(self):
        self.__flag.set()
