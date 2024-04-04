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

def is_format_correct():
    pass
def is_number_in_row(tablica,row,collum,number):
    pass
def find_empty_space(tablica):
    for row in tablica:
        for collum in tablica:
            if tablica[row][collum] == "0" :
                return ( row,collum)
def solve_sudoku():
    pass
def print_sudoku_board(tablica):
    