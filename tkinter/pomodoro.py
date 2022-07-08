import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
time = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(time)
    timer.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    ok.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1
    if reps==8:
        timer.config(text="break", fg=RED)
        countdown(LONG_BREAK_MIN*60)
    elif reps%2==0:
        timer.config(text="break", fg=PINK)
        countdown(SHORT_BREAK_MIN*60)
    elif reps%2!=0:
        timer.config(text="work", fg=GREEN)
        countdown(WORK_MIN*60)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    global time
    count_min=count//60
    count_sec=count%60
    if count_sec<10:
        count_sec = "0"+str(count_sec)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")    
    if count>0:
        time = window.after(1000, countdown, count-1)
    else:
        start_timer()
        ok["text"]="✓"*(reps//2)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.config(padx=100, pady=50, bg=YELLOW)

timer = tk.Label(bg=YELLOW, fg=GREEN, text="Timer", font=(FONT_NAME, 35, "bold"))
timer.grid(row=0, column=1)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = tk.PhotoImage(file="tkinter/tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

start = tk.Button(text="Start", command=start_timer)
start.grid(row=2, column=0)

reset = tk.Button(text="Reset", command=reset_timer)
reset.grid(row=2, column=2)

ok = tk.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
ok.grid(row=3, column=1)

window.mainloop()
