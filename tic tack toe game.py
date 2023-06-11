import tkinter as tk
from tkinter import messagebox
game_board = [['','',''],
              ['','',''],
              ['','','']]
current_player ='X'
def handle_click(row, col):
    global current_player
    if game_board[row][col] =='':
        game_board[row][col] = current_player
        buttons[row][col].config(text=current_player)                          
        winner =check_winner()
        if winner:
            messagebox.showinfo("Game Over", "Player " + winner + " wins!")
            reset_game()
        elif is_board_full():
            messagebox.showinfo("Game Over", "It is a draw game")
            reset_game()
        else:
            current_player ='X' if current_player =='Y'else'Y'
def check_winner():
    for row in range(3):
        if game_board[row][0] == game_board[row][1] == game_board[row][2] != '':
            return game_board[row][0]
    for col in range(3):
        if game_board[0][col] == game_board[1][col] == game_board[2][col] != '':
            return game_board[0][col]
    if game_board[0][0] == game_board[1][1] == game_board[2][2] != '':
        return game_board[0][0]
    if game_board[0][2] == game_board[1][1] == game_board[2][0] != '':
        return game_board[0][2]
    return None
def is_board_full():
    for row in range(3):
        for col in range(3):
            if game_board[row][col] == '':
                return False
    return True
def reset_game():
    global game_board, current_player
    game_board = [['','',''],
                  ['','',''],
                  ['','','']]
    current_player = 'Y'
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text='')
window = tk.Tk()
window.title("Tic-Tac-Toe Game")
buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(window, text='', width=12, height=7,
                          command=lambda r=row, c=col: handle_click(r, c))
        button.grid(row=row, column=col, padx=5, pady=5)
        button_row.append(button)
    buttons.append(button_row)
window.mainloop()