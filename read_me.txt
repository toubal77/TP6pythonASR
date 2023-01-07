#TOUBAL ZINE-EDDINE SID GROUPE3
#BENALI MOHAMMED YACINE SID GROUPE3
- l'exécution va être sur Pycharm, avec un exemple pour montre le déroulement du programme
1- la première des choses on va ouvrir 3 terminaux
	- sur chaque terminal on va mettre les commendes suivantes pour lancer le programme:
		- python node.py 1001 1
		  ensuite va nous affiche son ID: 185359819731349270315383770229510310318
		- python node.py 1002 0
		  ensuite va nous affiche son ID: 240070552096829844639334497754989862370
		- python node.py 1003 0
		  ensuite va nous affiche son ID: 128258526388925756176924412632579248747
	remarque: on principe le noeud 2 va être sélectionner perce-que il possede ID le plus grand
2- Après avoir lancé le programme, nous devons entre le numéro de port du voisin:
	- pour le terminal 1: son voisin c'est le numéro de port 1002
	- pour le terminal 2: son voisin c'est le numéro de port 1003
	- pour le terminal 3: son voisin c'est le numéro de port 1001
3- le noeud qui possède le token va nous demande de clique sur entre pour le libéré, apres cela le
   token vas etre envoye au noeud suivant "1002" ainsi son ID.
4- le noeud "1002" va recevoir ID et le TOKEN, il va compare son ID et ID qu'il a reçu,
   la comparaison va être entre (ID qu'il recu :185359819731349270315383770229510310318, son ID: 240070552096829844639334497754989862370),
   la comparaison va nous donne ID le plus grand -> 240070552096829844639334497754989862370
5- le noeud "1002" va libéré le TOKEN et envoyé ID qu'il a retourné après avoir fait la comparaison au noeud
   suivant "1003"
6- le noeud "1003" vas recevoir le TOKEN et ID 240070552096829844639334497754989862370 et va le comparer 
   avec son ID  128258526388925756176924412632579248747
7- le noeud va nous retourne ID le plus grand 240070552096829844639334497754989862370
	remarque: Après la participation de tous les noeuds a l'élection, ID qui a ete selectionne
	"240070552096829844639334497754989862370", ID va passe sur les noeuds jusqu'à 
	qu'il trouve son propriétaire
8- le noeud "1003" va libere le token et envoye ID selectionne a son voisin le noeud "1001"
9- le noeud "1001" va voir si il est le propriétaire du ID selectionne, il est pas donc va 
   libere le token et envoye ID au noeud suivant "1002"
10- le noeud "1002" recevera ID et verifie qu'il est le propriétaire, si le cas donc il declare que c'est
   lui le LEADER le noeud SELECTIONNE, et le programme s'arrete