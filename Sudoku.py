import numpy

class Sudoku:


    grid: list
    pool = numpy.array([3, 6, 2, 8, 1, 4, 7, 9, 5]) # pour les tests a la base

    def __init__(self, grid: list = []):
        self.grid = grid

    def createGridRandom(self):
        self.grid =  numpy.zeros(shape=(9,9)) # creer matrice
        for row in range (0,9):
            for col in range(0,9):
                self.grid[row][col] = random.randint(0,9)
                #Convertion en Int
                self.grid = numpy.array( self.grid, dtype=numpy.int) #transforme la liste en array et en int
        return self.grid

    def createSudokuResolved(self, numberoftime):
        grid_test = list("197648325682357491534291867341569782275184936869723514716835249923476158458912673")
        grid_test2 = list(map(int,grid_test))
        array_test = numpy.array(grid_test2)
        sudoku_test = array_test.reshape(9,9)
        self.grid = sudoku_test #attribut grid de ta classe sera sudoku test (en gros j'attribue cette valeur a ma classe)
        for i in range(0,numberoftime): ## le nbr de zeros qu'on veux lui donner
            self.grid[random.randint(0,8)][random.randint(0,8)] = 0

        return self.grid

    def unique(self): ## on l'utilse que pour checker si les numeros st uniques
        self.grid = self.grid.flatten()
        seen = set()
        return not any(i in seen or seen.add(i) for i in self.grid)

# def fonction qui utilise la fonction unique sur un tableau entier et
# retourne quand le sudoku est faux ""
    # def checkGrid(self):
    # #Mise a zero d'un compteur
    #     ct = 0
    #     for row in range (0,9):
    #     #chaque ligne

    #         print(self.unique(self.grid[row,:]).unique())
    #         ct +=1
    #         print(ct)
    #         if not self.unique(self.grid[row,:]):
    #         #si il trouve des valeurs non unique il exit
    #             return (print("le sudoku n'est pas bon, la ligne :"
    #                       ,row +1,"n'a pas que des valeurs unique"))

    #     for col in range(0,9):
    #     #chaque colone
    #         print(self.unique(self.grid[:,col]))
    #         ct +=1
    #         print(ct)
    #         if not self.unique(self.grid[:,col]):
    #         #si il trouve des valeurs non unique il exit
    #             return (print("le sudoku n'est pas bon, la colone :"
    #                       ,col +1,"n'a pas que des valeurs unique"))

    #     for i in range(0,7,3):
    #         for c in range(0,7,3):
    #         #chaque bloc
    #             print(self.unique(self.grid[i:i+3,c:c+3]))
    #             ct +=1
    #             print(ct)
    #             if not self.unique(self.grid[i:i+3,c:c+3]):
    #             #si il trouve des valeurs non unique il exit
    #                 return (print("le sudoku n'est pas bon le bloc"
    #                           ,"[",(i//3)+1,",",(c//3)+1,"]", "n'a pas que des valeurs unique"))
    #     return print("suuuuuuuuuuuuuuuuuuuuuu")
    
    def findCaseEmpty(self): # a function to find the first 0 and his position
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0 :
                    return row,col
        return None


    def is_valid_move(self, row, column, num): ## c'est le defSolve de Morgan (le self ne sers qu'à appliquer a une classe)
        # Vérifie si le numéro apparaît dans la même ligne
        if num in self.grid[row, :]:
            return False
        # Vérifie si le numéro apparaît dans la même colonne
        if num in self.grid[:, column]:
            return False
        # Trouver les coordonnées de départ du Block
        start_row = row // 3 * 3  ## si division totale tu peux partir nvo bloc
        start_column = column // 3 * 3  ## permet partir sur nouvelle 
        # Vérifie si le numéro apparaît dans un Block  (sous-grille 3x3)
        if num in self.grid[start_row:start_row+3, start_column:start_column+3]: 
            return False
        # Si aucune des vérifications n'échoue, on retourne True
        return True

    def solver(self):

        empty_cell = numpy.where(self.grid==0) ## renvoyer position des zeros
        if not empty_cell[0].size:
        # S'il n'y a pas de cellules vides, le sudoku est résolu
            return self.grid ## renvoie le self.grid si y a pas de valeurs vides

    # Variable  les positions (indices) de la cellule vide
        row, column = empty_cell[0][0], empty_cell[1][0]  ## on peut faire deux variables avec deux valeurs (a la base on se servait du set et code plus log, Kamel le trouve)

    # Parcours les nombres de 1 à 9
        for num in range(1, 10):
        # Vérifie si le numéro est valide pour la cellule donnée
            if self.is_valid_move( row, column, num):
            # Si la function valid_move est valide, on remplit la cellule avec le nombre
                self.grid[row, column] = num ## des qu'il trouve un zero il le remplace par ts les chiffres jusqu'à trouver le bon
            # Appel récurse de la fonction solveur sur la cellule suivante
                solution = self.solver()
                # print(self.grid)
                if solution is not None:
                # Si une solution est trouvée, on la retourne
                    return solution
            # Si aucune solution n'est trouvée, on remet la cellule à 0
                self.grid[row, column] = 0
    # Si aucun mouvement valide n'est trouvé, on renvoie None (pas de solution)
        return None