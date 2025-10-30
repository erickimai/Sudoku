import random
import asyncio

# ----------- Funções auxiliares -----------

def is_valid(board, num, row, col):
    for x in range(9):
        if x != col and board[row][x] == num:
            return False
    for x in range(9):
        if x != row and board[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if (i != row or j != col) and board[i][j] == num:
                return False
    return True


def TestaMatrizSudoku(M):
    for row_index, row in enumerate(M):
        for col_index, ele in enumerate(row):
            if ele != 0 and not is_valid(M, ele, row_index, col_index):
                return False
    return True


def GenMatrix(npp):
    Mat = [[0]*9 for _ in range(9)]
    numbers = []
    positions = []
    count = 0
    while count < npp:
        number = random.randrange(1, 10)
        numbers.append(number)
        row = random.randrange(9)
        col = random.randrange(9)
        position = (row, col)
        while position in positions:
            row = random.randrange(9)
            col = random.randrange(9)
            position = (row, col)
        positions.append(position)
        count += 1
    for k, (i, j) in enumerate(positions):
        Mat[i][j] = numbers[k]
    return Mat


# ----------- Sudoku com backtracking clássico -----------

def Sudoku(board, r, c):
    global solucoes, limite_solucoes

    # função auxiliar para encontrar próxima célula vazia
    def find_empty(start_row, start_col):
        for i in range(start_row, 9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None, None

    # encontra próxima posição vazia
    row, col = find_empty(r, c)

    if row is None:
        # solução completa encontrada
        solucoes += 1
        if solucoes <= limite_solucoes:
            print(f"\n* * * Matriz Completa – Solução {solucoes}")
            for linha in board:
                print(*linha)
            verifica_completa(board)
        return

    for num in range(1, 10):
        if is_valid(board, num, row, col):
            board[row][col] = num
            Sudoku(board, row, col)
            board[row][col] = 0  # backtrack


# ----------- Verificações finais -----------

def verifica_completa(board):
    def linhas_ok():
        return all(sorted(linha) == list(range(1, 10)) for linha in board)

    def colunas_ok():
        return all(sorted(board[i][j] for i in range(9)) == list(range(1, 10)) for j in range(9))

    def quadrados_ok():
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                nums = [board[i][j] for i in range(r, r + 3) for j in range(c, c + 3)]
                if sorted(nums) != list(range(1, 10)):
                    return False
        return True

    print("linhas OK * * * * * *" if linhas_ok() else "linhas incorretas")
    print("colunas OK * * * * * *" if colunas_ok() else "colunas incorretas")
    print("quadrados OK * * * * *" if quadrados_ok() else "quadrados incorretos")

    if linhas_ok() and colunas_ok() and quadrados_ok():
        print("* * * Matriz Completa e Consistente\n")


# ----------- Programa principal -----------

async def main():
    global solucoes, limite_solucoes
    limite_solucoes = 20
    while True:

        inp = input("Entre com o número de posições a preencher incialmente = ")
        if inp == "fim": break
        npp = int(inp)
        Mat = GenMatrix(npp)
        while not TestaMatrizSudoku(Mat):
            Mat = GenMatrix(npp)

        print("\n* * * Matriz inicial")
        for linha in Mat:
            print(linha)

        solucoes = 0
        try:
            await asyncio.wait_for(asyncio.to_thread(Sudoku, Mat, 0, 0), timeout=10.0)
        except asyncio.TimeoutError:
            print("A função Sudoku excedeu o tempo limite")

        if solucoes == 0:
            print("\nNenhuma solução encontrada dentro do tempo limite.")
        elif solucoes > limite_solucoes:
            print("\n*** Há mais soluções")


if __name__ == "__main__":
    asyncio.run(main())
