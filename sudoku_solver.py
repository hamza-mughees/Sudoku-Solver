class Sudoku:
    def __init__(self, grid):
        self.grid = grid
        self.__sol_cnt = 0
    
    def __str__(self):
        string = ""
        for row in self.grid:
            string = str(row) if string == "" else string + "\n" + str(row)
        return string
    
    def __is_empty(self, x, y):
        if self.grid[y][x] == 0: return True
        return False
    
    def __insert(self, n, x, y):
        self.grid[y][x] = n
    
    def __empty(self, x, y):
        self.grid[y][x] = 0
    
    def __current_box_first_cell(self, x, y):
        return (x//3) * 3, (y//3) * 3
    
    def __insert_possible(self, n, x, y):
        for i in range(9):
            if self.grid[i][x] == n: return False

        for i in range(9):
            if self.grid[y][i] == n: return False

        x_of_box, y_of_box = self.__current_box_first_cell(x, y)

        for i in range(3):
            for j in range(3):
                if self.grid[y_of_box + i][x_of_box + j] == n:
                    return False
        
        return True

    def solve(self):        # using back-tracking algorithm
        for y in range(9):
            for x in range(9):
                if self.__is_empty(x, y):
                    for n in range(1, 10):
                        if self.__insert_possible(n, x, y):
                            self.__insert(n, x, y)
                            self.solve()
                            self.__empty(x, y)
                    return
        self.__sol_cnt += 1
        print("\nSolution " + str(self.__sol_cnt))
        print(self)
        return
'''
if __name__ == '__main__':
    with open("\\Users\\hamza\\Documents\\VS Code\\Python\\Sudoku Solver\\input_sudoku.txt", "r") as text_file:
        grid = [row.split() for row in text_file]
    grid = [list(map(int, row)) for row in grid]
    puzzle = Sudoku(grid)
    puzzle.solve()
'''