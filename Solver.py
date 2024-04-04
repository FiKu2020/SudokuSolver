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
         pass #zrobic czy wartosc jest w kolumnie
    def find_empty_space(tablica):
        for row in tablica:
            for collum in tablica:
                if tablica[row][collum] == 0 :
                    return ( row,collum)
    def solve_sudoku():
        pass
    def print_sudoku_board(tablica):
        print(tablica)
