import Creator
import Main
import tkinter as tk

root = tk.Tk()
root.title("Password Generator")
root.geometry("800x600")

title = tk.Label(root, text="Password Generator", font=("Arial", 24))
title.pack(pady=20)
stc = tk.Label(root, text="Select the configurations:", font=("Arial", 18))
stc.pack(pady=20)

security_label = tk.Label(root, text="Security Level:", font=("Arial", 14))
security_label.pack(pady=10)
SecurityLvl = tk.StringVar(value="Md") 
select_level_low = tk.Radiobutton(root, text='Low', value='Lw', variable=SecurityLvl).pack(anchor='w')
select_level_medium = tk.Radiobutton(root, text='Medium', value='Md', variable=SecurityLvl).pack(anchor='w')
select_level_high = tk.Radiobutton(root, text='High', value='Hg', variable=SecurityLvl).pack(anchor='w')
select_level_extreme = tk.Radiobutton(root, text='Extreme', value='Ex', variable=SecurityLvl).pack(anchor='w')

type_label = tk.Label(root, text="Password Type:", font=("Arial", 14))
type_label.pack(pady=10)
type_ = tk.StringVar(value="Alphanumeric")
select_type_AN = tk.Radiobutton(root, text='Leters-only', value='Alphanumeric', variable=type_).pack(anchor='w')
select_type_PIN = tk.Radiobutton(root, text='PIN', value='Numeric_4', variable=type_).pack(anchor='w')
select_type_PIN6 = tk.Radiobutton(root, text='Six numbers', value='Numeric_6', variable=type_).pack(anchor='w')
select_type_ASCII = tk.Radiobutton(root, text='Normal', value='ASCII', variable=type_).pack(anchor='w')

saves = tk.Button(root, text="Saved Passwords", default="active", command=Main.SavedPasswords)
saves.pack(padx=20)
confirm = tk.Button(root, text="Confirm", default="active", command=lambda: Creator.makePassword(SecurityLvl.get(), type_.get()))
confirm.pack(pady=20)

root.mainloop()