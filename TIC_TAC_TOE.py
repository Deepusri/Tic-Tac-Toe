from tkinter import *
import random



from tkinter import messagebox


def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(users[1] + " Turn!"))

            elif check_winner() is True:
                label.config(text=(users[0] + " Wins"))
                messagebox.showinfo("user turn", "player1 winner ")


            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(users[0] + " Turn!"))

            elif check_winner() is True:
                label.config(text=(users[1] + " Wins"))
                messagebox.showinfo("user turn", "player2 winner ")


            elif check_winner() == "Tie":
                label.config(text="oohh it's Tie!")
                messagebox.showinfo("no turn", "it's TIE")


def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="Turquoise")
            buttons[row][1].config(bg="Turquoise")
            buttons[row][2].config(bg="Turquoise")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="Turquoise")
            buttons[1][column].config(bg="Turquoise")
            buttons[2][column].config(bg="Turquoise")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="Turquoise")
        buttons[1][1].config(bg="Turquoise")
        buttons[2][2].config(bg="Turquoise")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="Turquoise")
        buttons[1][1].config(bg="Turquoise")
        buttons[2][0].config(bg="Turquoise")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                

                buttons[row][column].config(bg="darkseagreen")
        return "Tie"

    else:
        return False






def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True





def new_game():
    global player

    player = random.choice(players)

    label.config(text=user + " Turn!")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="white")



window = Tk()
window.title("Tic-Tac-Toe")
window.configure(background="darkseagreen")

players = ["X", "O"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]



users = ["Player1", "Player2"]
user = random.choice(users)

label = Label(text=" WELCOME TO TIC-TAC-TOE", font=("Arial black", 20), bg='Darkseagreen', fg='black', bd=20, width=30)
label.pack(side="top")

label = Label(text=user + " Turn!", font=("Playball", 20), fg='black', bd=20, width=9)
label.pack(side="top")

reset_button = Button(window, text="Restart", font=("Lobster", 20), command=new_game, bg='peachpuff',height=2,width=10)
reset_button.pack(side="bottom")


frame = Frame(window, bg="saddlebrown")
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))

        

        buttons[row][column].grid(row=row, column=column, padx=10, pady=10)
window.mainloop()
