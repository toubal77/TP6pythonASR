#TOUBAL ZINE-EDDINE SID GROUPE3
#BENALI MOHAMMED YACINE SID GROUPE3

from lib import *
from component_node.part_in import *
from component_node.part_out import *

PORT_IN = int(sys.argv[1])
Have_Token = int(sys.argv[2]) # 1 have token | 0 don't have token

elect = Elect(PORT_IN)
idElect = elect.id
print("ID du noeud généné est: ", int(idElect))

Sd_Out = Part_Out(elect)

Sd_Out.port_next_neighbor = int(input("Numéro de port du voisin: "))
Sd_Out.start()

Sd_In = Part_In(PORT_IN, Have_Token, Sd_Out,elect)
Sd_In.start()

