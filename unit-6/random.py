import tkinter as tk
import random

COLS = 10
ROWS = 20
SIZE = 25

SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1],
     [1, 1]],
    [[0, 1, 0],
     [1, 1, 1]],
    [[0, 1, 1],
     [1, 1, 0]],
    [[1, 1, 0],
     [0, 1, 1]],
    [[1, 0, 0],
     [1, 1, 1]],
    [[0, 0, 1],
     [1, 1, 1]],
]
COLORS = ["CYAN", "YELLOW", "PURPLE", "GREEN", "RED", "BLUE", "ORANGE"]

board = []
score = 0
lines = 0
level = 1
game_over = False
loop_id = None

shape = []
color = ""
px = 0
py = 0


def make_empty_board():
    return [[0] * COLS for _ in range(ROWS)]


def new_piece():
    global shape, color, px, py, game_over
    i = random.randint(0, 6)
    shape = SHAPES[i]
    color = COLORS[i]
    px = COLS // 2 - len(shape[0]) // 2
    py = 0
    if not can_move(shape, px, py):
        game_over = True


def can_move(s, x, y):
    for row in range(len(s)):
        for col in range(len(s[row])):
            if s[row][col]:
                nx = x + col
                ny = y + row
                if nx < 0 or nx >= COLS:
                    return False
                if ny < 0 or ny >= ROWS:
                    return False
                if board[ny][nx] != 0:
                    return False
    return True


def rotate(s):
    return [list(row) for row in zip(*s[::-1])]


def lock_piece():
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col]:
                board[py + row][px + col] = color


def clear_lines():
    global board, score, lines, level
    full_rows = [row for row in board if all(row)]
    count = len(full_rows)
    if count > 0:
        board = [row for row in board if not all(row)]
        for i in range(count):
            board.insert(0, [0] * COLS)
        lines += count
        score += count * 100
        level = lines // 10 + 1
        update_labels()


def update_labels():
    score_label.config(text=f"Score: {score}")
    lines_label.config(text=f"Lines: {lines}")
    level_label.config(text=f"Level: {level}")


def draw_block(x, y, color):
    x1 = x * SIZE
    y1 = y * SIZE
    x2 = x1 + SIZE
    y2 = y1 + SIZE
    canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")


def draw():
    canvas.delete("all")
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col]:
                draw_block(col, row, board[row][col])
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col]:
                draw_block(px + col, py + row, color)
    if game_over:
        canvas.create_text(COLS * SIZE // 2, ROWS * SIZE // 2,
                           text="GAME OVER", fill="white",
                           font=("Arial", 24, "bold"))


def game_loop():
    global py, loop_id
    if game_over:
        return
    if can_move(shape, px, py + 1):
        py += 1
    else:
        lock_piece()
        clear_lines()
        new_piece()
    draw()
    if not game_over:
        loop_id = window.after(max(100, 500 - (level - 1) * 40), game_loop)


def key_press(event):
    global px, py, shape
    if game_over:
        return
    if event.keysym == "Left":
        if can_move(shape, px - 1, py):
            px -= 1
    elif event.keysym == "Right":
        if can_move(shape, px + 1, py):
            px += 1
    elif event.keysym == "Down":
        if can_move(shape, px, py + 1):
            py += 1
    elif event.keysym == "Up":
        rotated = rotate(shape)
        if can_move(rotated, px, py):
            shape = rotated
    elif event.keysym == "space":
        while can_move(shape, px, py + 1):
            py += 1
        lock_piece()
        clear_lines()
        new_piece()
    draw()


def restart():
    global board, score, lines, level, game_over, loop_id
    if loop_id is not None:
        window.after_cancel(loop_id)
        loop_id = None
    board = make_empty_board()
    score = 0
    lines = 0
    level = 1
    game_over = False
    update_labels()
    new_piece()
    draw()
    loop_id = window.after(500, game_loop)


window = tk.Tk()
window.title("Tetris Game")

canvas = tk.Canvas(window, width=COLS * SIZE, height=ROWS * SIZE, bg="black")
canvas.pack()
score_label = tk.Label(window, text="Score: 0")
score_label.pack()
lines_label = tk.Label(window, text="Lines: 0")
lines_label.pack()
level_label = tk.Label(window, text="Level: 1")
level_label.pack()
restart_button = tk.Button(window, text="Restart", command=restart)
restart_button.pack()
window.bind("<KeyPress>", key_press)
restart()
window.mainloop()