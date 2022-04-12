def transpose(board):
    transposedBoard = []
    for i in range(len(board[0])):
        transposedBoard.append([])
        for j in range(len(board[0])):
            transposedBoard[i].append(board[j][i])
    return transposedBoard


def reverse(board):
    reverseBoard = []
    for i in range(len(board[0])):
        reverseBoard.append([])
        for j in range(len(board[0])):
            reverseBoard[i].append(board[i][len(board[0]) - j - 1])
    return reverseBoard


def merge(board):
    done = False
    for i in range(len(board[0])):
        for j in range(len(board[0]) - 1):
            if board[i][j] == board[i][j + 1] and board[i][j] != "-":
                board[i][j] *= 2
                board[i][j + 1] = "-"
                done = True
    return board, done


def coverBoard(board):
    newBoard = []
    for i in range(len(board[0])):
        row = []
        for j in range(len(board[0])):
            row.append("-")
        newBoard.append(row)

    done = False
    for i in range(len(board[0])):
        count = 0
        for j in range(len(board[0])):
            if board[i][j] != "-":
                newBoard[i][count] = board[i][j]
                if j != count:
                    done = True
                count += 1
    return newBoard, done


def right(board):
    print("right")
    board = reverse(board)
    board, done = coverBoard(board)
    board, done = merge(board)
    board = reverse(board)
    return board, done


def left(board):
    print("left")
    board, done = coverBoard(board)
    board, done = merge(board)
    return board, done


def down(board):
    print("down")
    board = transpose(board)
    board = reverse(board)
    board, done = coverBoard(board)
    board, done = merge(board)
    board = reverse(board)
    board = transpose(board)
    return board, done


def up(board):
    print("up")
    board = transpose(board)
    board, done = coverBoard(board)
    board, done = merge(board)
    board = transpose(board)
    return board, done
