import numpy
import random


class Sudoku:

    grid: list
    difficulty = ''

    def __init__(self, grid: list = [], ):
        self.grid = grid

    def createGridRandom(self):
        self.grid =  numpy.zeros(shape=(9,9))
        for row in range (0,9):
            for col in range(0,9):
                self.grid[row][col] = random.randint(0,9)
                #Convertion en Int
                self.grid = numpy.array( self.grid, dtype=numpy.int)
        return self.grid

    def createSudokuResolved(self, numberoftime):
        grid_test = list("197648325682357491534291867341569782275184936869723514716835249923476158458912673")
        grid_test2 = list(map(int,grid_test))
        array_test = numpy.array(grid_test2)
        sudoku_test = array_test.reshape(9,9)
        self.grid = sudoku_test
        for i in range(0,numberoftime):
            self.grid[random.randint(0,8)][random.randint(0,8)] = 0

        return self.grid


    def unique(self,x):
    # if x.type
        flatten_x = x.flatten()
        flatten_x_copy = flatten_x
        a = flatten_x[flatten_x_copy!=0]
        seen = set()
        return not any(i in seen or seen.add(i) for i in a)

# def fonction qui utilise la fonction unique sur un tableau entier et
# retourne quand le sudoku est faux ""
    def checkGrid(self):
    #Mise a zero d'un compteur
        ct = 0
        for row in range (0,9):
        #chaque ligne

            print(self.unique(self.grid[row,:]))
            ct +=1
            print(ct)
            if not self.unique(self.grid[row,:]):
            #si il trouve des valeurs non unique il exit
                return (print("le sudoku n'est pas bon, la ligne :"
                          ,row +1,"n'a pas que des valeurs unique"))

        for col in range(0,9):
        #chaque colone
            print(self.unique(self.grid[:,col]))
            ct +=1
            print(ct)
            if not self.unique(self.grid[:,col]):
            #si il trouve des valeurs non unique il exit
                return (print("le sudoku n'est pas bon, la colone :"
                          ,col +1,"n'a pas que des valeurs unique"))

        for i in range(0,7,3):
            for c in range(0,7,3):
            #chaque bloc
                print(self.unique(self.grid[i:i+3,c:c+3]))
                ct +=1
                print(ct)
                if not self.unique(self.grid[i:i+3,c:c+3]):
                #si il trouve des valeurs non unique il exit
                    return (print("le sudoku n'est pas bon le bloc"
                              ,"[",(i//3)+1,",",(c//3)+1,"]", "n'a pas que des valeurs unique"))
        return print("suuuuuuuuuuuuuuuuuuuuuu")
    def findCaseEmpty(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0 :
                    return row,col
        return None


    def is_valid_move(self, row, column, num):
        # Vérifie si le numéro apparaît dans la même ligne
        if num in self.grid[row, :]:
            return False
        # Vérifie si le numéro apparaît dans la même colonne
        if num in self.grid[:, column]:
            return False
        # Trouver les coordonnées de départ du Block
        start_row = row // 3 * 3
        start_column = column // 3 * 3
        # Vérifie si le numéro apparaît dans un Block  (sous-grille 3x3)
        if num in self.grid[start_row:start_row+3, start_column:start_column+3]:
            return False
        # Si aucune des vérifications n'échoue, on retourne True
        return True

    def solver(self):

        empty_cell = numpy.where(self.grid==0)
        if not empty_cell[0].size:
        # S'il n'y a pas de cellules vides, le sudoku est résolu
            return self.grid

        row, column = empty_cell[0][0], empty_cell[1][0]
        # Parcours les nombres de 1 à 9
        for num in range(1, 10):

        # Vérifie si le numéro est valide pour la cellule donnée
            if self.is_valid_move( row, column, num):

            # Si la function valid_move est valide, on remplit la cellule avec le nombre
                self.grid[row, column] = num
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


    def grid_1line(self):
        self.grid= numpy.zeros((9, 9),int)
        sample = numpy.array(random.sample(range(1, 10), 9))
        self.grid[0,:] = sample
        return

    def level(self) :
        self.difficulty = input("Veuillez entrée votre difficulté : facile ou moyen ou difficile.")
        self.difficulty = self.difficulty.lower()
        if self.difficulty == 'facile':
            self.difficulty = 1
        if self.difficulty == 'moyen':
            self.difficulty = 2
        if self.difficulty == 'difficile':
            self.difficulty = 3
        return self.difficulty

    def creator(self):
        self.level()
        if self.difficulty == 1 or self.difficulty  == 2 or self.difficulty  == 3 :
            self.grid_1line()
            self.solver()
            for i in range(0,40 + self.difficulty *6 ):
                self.grid[random.randint(0,8)][random.randint(0,8)]=0
            return
        else:
            return self.creator()
