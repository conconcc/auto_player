import tkinter as tk
import auto_clc as ac
import auto_youtube as ay

def show_buttons():

    button_left.grid(row=0, column=0)
    button_right.grid(row=0, column=2)
    button_main.grid(row=0, column=1)
def show_youtube_buttons():

    # youtube, clc 버튼 보이기
    button_youtube.grid(row=0, column=0)
    button_stop.grid(row=0, column=1)
    button_clc.grid(row=0, column=2)
    button_undo.grid(row=1, column=1)

def hide_buttons():
    # 모든 버튼 숨기기
    button_left.grid_forget()
    button_right.grid_forget()
    button_main.grid_forget()
    button_youtube.grid_forget()
    button_clc.grid_forget()
    button_stop.grid_forget()

def on_left_click():
    global side
    print("Left button clicked")
    hide_buttons()
    show_youtube_buttons()
    side="left"
def on_right_click():
    global side
    print("Right button clicked")
    hide_buttons()
    show_youtube_buttons()
    side="right"
def on_main_click():
    print("Main button clicked")
    hide_buttons()
    show_youtube_buttons()
    global side
    side="main"
def on_youtube_click():
    
    print("YouTube button clicked")
    ay.run(side)
def on_clc_click():
    
    print("CLC button clicked")
    ac.run(side)  

def undo_buttons():
    hide_buttons()
    show_buttons()
def all_stop():
    quit()

# Tkinter 윈도우 생성
window = tk.Tk()
window.title("buttons")

# 버튼 생성
button_left = tk.Button(window, text="Left", command=on_left_click)
button_right = tk.Button(window, text="Right", command=on_right_click)
button_main = tk.Button(window, text="Main", command=on_main_click)
button_youtube = tk.Button(window, text="YouTube", command=on_youtube_click)
button_clc = tk.Button(window, text="CLC", command=on_clc_click)
button_stop = tk.Button(window, text="Stop", command=all_stop)
button_undo = tk.Button(window, text="Undo", command=undo_buttons)

#left, right, main 세 가지 버튼 보이기
show_buttons()

window.mainloop()
