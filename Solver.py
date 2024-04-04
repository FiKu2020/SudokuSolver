class Sudoku_Solver(self):

    TablicaNr1 = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

    def is_format_correct(tablica):
        if len(tablica) !=9:
            return False
        for row in tablica:
            if len(row) !=9:
                 return False #do zrobienia: sprawdzanie czy wartosc nie jest litera albo wieksza od 9
    
    def is_number_in_row(tablica,row,collum,number):
        for i in range(9):
            if tablica[row][i] == number:
                    return True
            else:
                    return False
    def is_number_in_collum(tablica,row,collum,number):
         for i in range(9): #zrobic czy wartosc jest w kolumnie
               if tablica[i][collum] == number:
                    return True
               else:
                    return False
    def find_empty_space(tablica):
        for row in tablica:
            for collum in tablica:
                if tablica[row][collum] == 0 :
                    return ( row,collum)
                else:
                     return False
    def solve_sudoku(tablica):
        spaces_to_replace = Sudoku_Solver.find_empty_space(tablica)
        if spaces_to_replace == False:
             return True
        row , collum = spaces_to_replace
        
    def print_sudoku_board(tablica):
        print(tablica)
