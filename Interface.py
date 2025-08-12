from Creator import MakePassword
import tkinter as tk

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

title = tk.Label(root, text="Password Generator", font=("Arial", 24))
title.pack(pady=20)
stc = tk.Label(root, text="Select the configurations:", font=("Arial", 18))
stc.pack(pady=20)
confirm = tk.Button(root, text="Confirm", default="active", command=MakePassword)
confirm.pack(pady=20)

root.mainloop()