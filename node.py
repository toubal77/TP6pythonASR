from lib import *
from component_node.part_in import *
from component_node.part_out import *

port_in = int(sys.argv[1])
have_token = int(sys.argv[2])

sd_out = Part_Out()

sd_out.port_next_neighbor = int(input("Numero de port du voisin: "))
#with open("etudiant.txt", "a", encoding="utf-8") as f:
#    f.write(sd_out.port_next_neighbor + " \n")
sd_out.start()

sd_in = Part_In(port_in, have_token, sd_out)
sd_in.start()
