import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, height=100, bg="red")
frame1.pack(fill=tk.BOTH)

frame2 = tk.Frame(master=window, height=50, bg="yellow")
frame2.pack(fill=tk.BOTH)

frame3 = tk.Frame(master=window, height=25, bg="blue")
frame3.pack(fill=tk.BOTH)

window.mainloop()
