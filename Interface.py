import Creator
import tkinter as tk

root = tk.Tk()
root.title("Password Generator")
root.geometry("800x600")

title = tk.Label(root, text="Password Generator", font=("Arial", 24))
title.pack(pady=20)
stc = tk.Label(root, text="Select the configurations:", font=("Arial", 18))
stc.pack(pady=20)

security_level = tk.Label(root, text="Security Level:", font=("Arial", 14))
security_level.pack(pady=10)
SecurityLvl = tk.StringVar(value="Md") 
select_level_low = tk.Radiobutton(root, text='Low', value='Lw', variable=SecurityLvl).pack(anchor='w')
select_level_medium = tk.Radiobutton(root, text='Medium', value='Md', variable=SecurityLvl).pack(anchor='w')
select_level_high = tk.Radiobutton(root, text='High', value='Hg', variable=SecurityLvl).pack(anchor='w')
select_level_extreme = tk.Radiobutton(root, text='Extreme', value='Ex', variable=SecurityLvl).pack(anchor='w')

confirm = tk.Button(root, text="Confirm", default="active", command=Creator.makePassword(SecurityLvl.get()))
confirm.pack(pady=20)

root.mainloop()