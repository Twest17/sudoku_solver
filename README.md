# sudoku_solver

1.find empty cell
if not empty then sudoku solved

2.try paste every digit 1-9 into it:
    if no conflict in row, column and box then recursively repeat steps 1-2
    if conflict, then erase pasted digit and try next digit
    if no digit can be placed into empty cell, then return back in recurse
if returned back to root and no digit can be placed then sudoku doesn't have solution