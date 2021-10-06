import keyboard #importation de la bibliothèque keyboard pour détecter les frappes de clavier

class Carte:
    """
    classe Carte qui ouvre le fichier texte et le convertit en une carte à afficher
    carte : le nom du fichier en string
    renvoie la carte à afficher
    contient la position de tous les murs, de tous les espaces, de la sortie et de l'entrée'
    """
    
    texte = ''
    pos_sortie = None


    def __init__(self,carte):
        Carte.texte = carte #variable global au programme pour pouvoir être appeler n'importe où
        cartes = open(carte)
        self.carte = [ligne[:-1] for ligne in cartes] # le fichier texte est convertie en tableau
        self.mur = [] 
        self.espace = [] 
        self.posentree = None
      
        
    def _gettexte(self): # Méthode qui renvoie la carte choisie
        return self.texte
    
    
    def _conversion(self): #Méthode qui convertit le fichier texte en une carte affichable
        res = ''
        Lem = Lemming()
        for colonnes in range(len(self.carte)):
            for lignes in range(len(self.carte[colonnes])):
                if colonnes == Lem.pos_lemming[0] and lignes == Lem.pos_lemming[1] :
                    res += 'x'
                    
                elif self.carte[colonnes][lignes] == '#':
                    res += Case._bloc(self.carte[colonnes][lignes])
                    self.mur.append((colonnes,lignes))
                elif self.carte[colonnes][lignes] == ' ':
                    res += Case._bloc(self.carte[colonnes][lignes])
                    self.espace.append((colonnes,lignes))
                elif self.carte[colonnes][lignes] == 'E':
                    res += Case._bloc(self.carte[colonnes][lignes])
                    self.posentree = (colonnes,lignes)
                elif self.carte[colonnes][lignes] == 'S':
                    res += Case._bloc(self.carte[colonnes][lignes])
                    Carte.pos_sortie = [colonnes,lignes]                      
            res += '\n'
        return res        

        
    def __repr__(self): # Méthode qui affiche la carte convertie
        impr = self._conversion()
        return impr

        
    def _getposmur(self): # Méthode qui renvoie une liste contenant la position de tous les murs
        self.__repr__()
        return self.mur
    
    
    def _getposspace(self): # Méthode qui renvoie une liste contenant la position de tous les espaces
        self.__repr__()
        return self.espace
    
    
    def _getposentree(self): # Méthode qui renvoie une liste contenant la position de l'entrée
        return self.posentree
    
    
    def _getpossortie(): # Méthode qui renvoie une liste contenant la position de la sortie
        return Carte.pos_sortie
    
    

class Case:
    """
    classe Case qui prend un caractère du fichier texte et renvoie un caractère affichable pour la carte
    bloc: un caractère du fichier texte
    retourne un caractère affichable
    """
      
    def _bloc(bloc):
        
        if bloc == '#':
            return '▓'
        
        elif bloc == 'S':
            return '@'
        
        elif bloc == 'E':
            return 'E'  
        
        elif bloc == ' ':
            return ' '
        
            
        
    
class Lemming(Carte):
    """
    classe Lemming qui contient les informations sur les lemmings et le fait avancer
    position : position de départ, devant l'entrée | pos_lemming : la position actuelle du lemming
    direction : direction de départ, vers la droite | direct_lem : la direction actuelle du lemming
    Map : la carte jouée
    Contient la position et la direction du lemming
    """
    
    def __init__(self,position=[1,1],direction=1):
        self.pos_lemming = position
        self.direct_lemming = direction
        return None
    

    def _avancer(self): #Méthode qui fait avancer le lemming de une case
        Map = Carte(Carte.texte)
        
        if Map.carte[self.pos_lemming[0]+1][self.pos_lemming[1]] == ' ': #Si la case en dessous du lemming est un espace, il descend
            self.pos_lemming[0]+= 1            
        
        elif Map.carte[self.pos_lemming[0]][self.pos_lemming[1]+self.direct_lemming] == '#' or Map.carte[self.pos_lemming[0]][self.pos_lemming[1]+self.direct_lemming] == 'x' :             #Si la case à côté du lemming dans sa direction est un mur ou un lemming
            self.direct_lemming = -self.direct_lemming # On change sa direction
            self.pos_lemming[1]+=self.direct_lemming # On le fait avancer de une case
        
        elif Map.carte[self.pos_lemming[0]][self.pos_lemming[1]+self.direct_lemming] == 'S':
            Jeu.sorties +=1 # Si un lemming atteint la sortie on ajoute 1 à la variable sorties
 
        else:
            self.pos_lemming[1]+=self.direct_lemming 
            
        return self.pos_lemming
    
    
    def _getposlem(self): #Méthode qui renvoie la position du lemming
        return self.pos_lemming        


           

class Jeu:
    """
    classe Jeu qui affiche la carte et fait avancer le lemming en fonction des frappes de l'utilisateur
    screen : la carte à afficher
    Lem : la classe Lemming est appelée
    sorties : le nombre de lemmings sortis
    contient l'écran et le nombre de lemming sortis
    """
       
    screen = None
    Lem = Lemming()
    sorties = 0
    
    def __init__(self,nb_lem,carte):
        self.nb_lem = nb_lem
        Jeu.screen = Carte(carte)
        return None


    def start(self): # Méthode qui affiche la carte et fait avancer le lemming en fonction de la pression de la touche espace par l'utilisateur
        print('appuyez sur espace pour avancer')  
        while True:
            if keyboard.read_key() == "space":
                print('\n' *10)
                print(Jeu.screen)
                Jeu.Lem._avancer()
                if keyboard.read_key() == "esc": #Sortie du jeu si la touche Echap est pressée
                    break 
                elif Jeu.sorties == self.nb_lem:
                    break
        return None

 
def lancer():
    """
    fonction qui prend le nombre de lemmings et le choix de la carte par l'utilisateur et lance le jeu
    nb_lems : un entier
    carte : un string
    renvoie None
    Affiche le jeu
    """
        
    nb_lems = int(input('Entrez le nombre de Lemmings: '))
    Map_1 = Carte('Map_1.txt')
    Map_2 = Carte('Map_2.txt')
    print(Map_1,'\n','1')
    print(Map_2,'\n','2')
    carte = int(input('Choississez la carte: '))
    if carte == 1:        
        Game = Jeu(nb_lems,"Map_1.txt")  
    elif carte == 2:
        Game = Jeu(nb_lems,"Map_2.txt") 
    Game.start()
      