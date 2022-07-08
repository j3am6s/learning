import tkinter as tk

window = tk.Tk()
window.minsize()
window.config(padx=50, pady=50)

#is equal to LABEL
is_equal_to = tk.Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

#miles ENTRY
input = tk.Entry(width=10)
input.grid(row=0, column=1)

#miles LABEL
miles = tk.Label(text="Miles")
miles.grid(row=0, column=2)

#km result LABEL
km_result = tk.Label(text="0")
km_result.grid(row=1, column=1)

#km LABEL
km = tk.Label(text="km")
km.grid(row=1, column=2)

#calculate BUTTON
def convert():
    km_result["text"] = round(float(input.get())*1.609344)
calculate = tk.Button(text="calculate", command=convert)
calculate.grid(row=2, column=1)

window.mainloop()
