import random
import numpy as np
import matplotlib.pyplot as plt


def create_board():
    return np.zeros((3, 3), dtype=int)


def place(board, player, position):
    board[position] = player


def possibilities(board):
    return np.array(np.where(board == 0)).T


def random_place(board, player):
    rem_pos = possibilities(board)
    pos = tuple(random.choice(rem_pos))
    board[pos] = player


def row_win(board, player):
    return [player, player, player] in board.tolist()


def col_win(board, player):
    return [player, player, player] in board.T.tolist()


def diag_win(board, player):
    return [player, player, player] == np.diag(board).tolist() or [
        player,
        player,
        player,
    ] == np.diag(np.fliplr(board)).tolist()


def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner


def play_game():
    board = create_board()
    while True:
        for player in [1, 2]:
            winner = evaluate(board)
            if winner in [1, 2]:
                return winner
            elif winner == -1:
                return winner
            else:
                random_place(board, player)


def play_center_game():
    board = create_board()
    board[1, 1] = 1
    while True:
        for player in [2, 1]:
            winner = evaluate(board)
            if winner in [1, 2]:
                return winner
            elif winner == -1:
                return winner
            else:
                random_place(board, player)


def play_corner_game():
    board = create_board()
    corner_pos = [(0, 0), (0, 2), (2, 0), (2, 2)]
    board[random.choice(corner_pos)] = 1
    while True:
        for player in [2, 1]:
            winner = evaluate(board)
            if winner in [1, 2]:
                return winner
            elif winner == -1:
                return winner
            else:
                random_place(board, player)


def play_cross_game():
    board = create_board()
    corner_pos = [(0, 1), (1, 0), (1, 2), (2, 1)]
    board[random.choice(corner_pos)] = 1
    while True:
        for player in [2, 1]:
            winner = evaluate(board)
            if winner in [1, 2]:
                return winner
            elif winner == -1:
                return winner
            else:
                random_place(board, player)


results1, results2, results3, results4 = [], [], [], []
for i in range(10000):
    win1 = play_game()
    win2 = play_center_game()
    win3 = play_corner_game()
    win4 = play_cross_game()
    results1.append(win1)
    results2.append(win2)
    results3.append(win3)
    results4.append(win4)

labels = ["Player 1", "Player 2", "Draw"]

plot1 = [results1.count(i) for i in [1, 2, -1]]
plot2 = [results2.count(i) for i in [1, 2, -1]]
plot3 = [results3.count(i) for i in [1, 2, -1]]
plot4 = [results4.count(i) for i in [1, 2, -1]]

x = np.arange(len(labels))
width = 0.2

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 0.5, plot1, width, label="Random")
rects2 = ax.bar(x - width / 1, plot2, width, label="Central")
rects3 = ax.bar(x, plot3, width, label="Corner")
rects4 = ax.bar(x + width / 1, plot4, width, label="Cross")

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate(
            "{}".format(height),
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha="center",
            va="bottom",
        )


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)

fig.tight_layout()

plt.show()