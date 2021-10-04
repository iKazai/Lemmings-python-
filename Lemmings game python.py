import time
import os
import time

class Carte:   
    texte = ''
    pos_sortie = None


    def __init__(self,carte):
        Carte.texte = carte
        cartes = open(carte)
        self.carte = [ligne[:-1] for ligne in cartes]
        self.mur = []
        self.espace = [] 
        self.posentree = None
      
        
    def _gettexte(self):
        return self.texte
    
    
    def _conversion(self):
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

        
    def __repr__(self):
        impr = self._conversion()
        return impr

        
    def _getposmur(self):
        self.__repr__()
        return self.mur
    
    
    def _getposspace(self):
        self.__repr__()
        return self.espace
    
    
    def _getposentree(self):
        return self.posentree
    
    
    def _getpossortie():
        return Carte.pos_sortie
    
    

class Case:       
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
    def __init__(self,position=[1,1],direction=1):
        self.pos_lemming = position
        self.direct_lemming = direction
        return None
    

    def _avancer(self):
        Map = Carte(Carte.texte)
        
        if Map.carte[self.pos_lemming[0]+1][self.pos_lemming[1]] == ' ':
            self.pos_lemming[0]+= 1          
        
        elif Map.carte[self.pos_lemming[0]][self.pos_lemming[1]+1] == '#' or Map.carte[self.pos_lemming[0]][self.pos_lemming[1]+1] == 'x' :
            self.direct_lemming = -self.direct_lemming
            self.pos_lemming[1]+=self.direct_lemming
                       
        else:
            self.pos_lemming[1]+=self.direct_lemming
            
        return self.pos_lemming
    
    
    def _getposlem(self):
        return self.pos_lemming        
        

    def _sortie(self):
        self.compteur = 0
        if self._getposlem() == Carte._getpossortie():
            self.compteur += 1
        return self.compteur 
 
    
           

class Jeu:
       
    screen = None
    Lem = Lemming()
    
    def __init__(self,nb_lem,carte):
        self.nb_lem = nb_lem
        Jeu.screen = Carte(carte)
        return None

    
    def lancer(self):
        debut = time.time()
        while time.time() < debut+300 or self.nb_lem-Lem._sortie()==0:
            print(Jeu.screen)
            time.sleep(1.1)
            print('\n' *20)
            Jeu.Lem._avancer()
            
    def reset(self):
        Lem.pos_lemming = [1,1]
        
            
            
        
    #fait avancer le temps
    #fait entrer un certain nombre de lemmings séparés d'un certain temps
    #limite qui assure que le jeu se termine (temps imparti)