import tkinter as tk


window = tk.Tk()
window.minsize()
window.config(padx=10, pady=10)

label = tk.Label(text="chrono", fg="red", font=("Courrier", 30))
label.grid(row=0, column=0, columnspan=2)

chronometre = tk.Label(text="00:00", font=("Courrier", 25), pady=20)
chronometre.grid(row=1, column=0, columnspan=2)

def start_chrono():
    chrono(time)

def chrono(time):
    global timer
    minutes = time//60
    secondes = time%60
    if minutes<10:
        minutes = f"0{minutes}"
    if secondes<10:
        secondes = f"0{secondes}"
    chronometre["text"] = f"{minutes}:{secondes}"
    timer=window.after(1000, chrono, time+1)

timer = None
time = 0
start = tk.Button(text="start", width=8, command=start_chrono)
start.grid(row=2, column=0)

def stop_chrono():
    global time
    window.after_cancel(timer)
    time=0
    chronometre["text"]="00:00"

stop = tk.Button(text="stop", width=8, command=stop_chrono)
stop.grid(row=2, column=1)


window.mainloop()
