def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:  # -1'in boş hücreyi temsil ettiğini düşünelim
                return r, c
    return None, None  # Puzzle içinde boş (-1) hücre yok demektir.

def is_valid(puzzle, guess, row, col):
    # Satır kontrolü yapar
    if guess in puzzle[row]:
        return False

    # Sütun kontrolü yapar
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # 3x3 kare kontrolü yapar
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)

    # Eğer dolu bir yer yoksa, işlem tamamlanmış demktir
    if row is None:
        return True

    for guess in range(1, 10):  # 1'den 9'a kadar olan sayıları tek tek dener
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess

            if solve_sudoku(puzzle):
                return True

        puzzle[row][col] = -1  # Tahmini sıfır.

    return False  # Geçerli bir çözüm yok demektir.

# Sudoku Bulmacasını Başlatır
puzzle = [
    [5, 3, -1, -1, 7, -1, -1, -1, -1],
    [6, -1, -1, 1, 9, 5, -1, -1, -1],
    [-1, 9, 8, -1, -1, -1, -1, 6, -1],
    [8, -1, -1, -1, 6, -1, -1, -1, 3],
    [4, -1, -1, 8, -1, 3, -1, -1, 1],
    [7, -1, -1, -1, 2, -1, -1, -1, 6],
    [-1, 6, -1, -1, -1, -1, 2, 8, -1],
    [-1, -1, -1, 4, 1, 9, -1, -1, 5],
    [-1, -1, -1, -1, 8, -1, -1, 7, 9]
]

    # ... geri kalan kısımları doldurun


# Bulmacayı Çöz
if solve_sudoku(puzzle):
    print("Sudoku Çözüldü:")
    for row in puzzle:
        print(row)
else:
    print("Çözüm bulunamadı.")
