import Creator
import Main
import tkinter as tk

root = tk.Tk()

content = tk.Frame(root)
content.pack(fill='both', expand=True)

root.title("Password Generator")
root.geometry("1280x720")

title = tk.Label(content, text="Password Generator", font=("Arial", 24))
stc = tk.Label(content, text="Select the configurations:", font=("Arial", 18))

security_label = tk.Label(content, text="Security Level:", font=("Arial", 14))

SecurityLvl = tk.StringVar(value="Md") 
select_level_low = tk.Radiobutton(content, text='Low', value='Lw', variable=SecurityLvl)
select_level_medium = tk.Radiobutton(content, text='Medium', value='Md', variable=SecurityLvl)
select_level_high = tk.Radiobutton(content, text='High', value='Hg', variable=SecurityLvl)
select_level_extreme = tk.Radiobutton(content, text='Extreme', value='Ex', variable=SecurityLvl)

type_label = tk.Label(content, text="Password Type:", font=("Arial", 14))
type_ = tk.StringVar(value="Alphanumeric")

select_type_AN = tk.Radiobutton(content, text='Letters-only', value='Alphanumeric', variable=type_)
select_type_PIN = tk.Radiobutton(content, text='PIN', value='Numeric_4', variable=type_)
select_type_PIN6 = tk.Radiobutton(content, text='Six numbers', value='Numeric_6', variable=type_)
select_type_ASCII = tk.Radiobutton(content, text='Normal', value='ASCII', variable=type_)

saves = tk.Button(content, text="Saved Passwords", default="active", command=Main.SavedPasswords)
confirm = tk.Button(content, text="Confirm", default="active", command=lambda: Creator.makePassword(SecurityLvl.get(), type_.get()))

# Layout widgets
title.grid(row=0, column=0, columnspan=4, pady=20)
stc.grid(row=1, column=0, columnspan=4, pady=10)

security_label.grid(row=2, column=0, columnspan=4, pady=10)

select_level_low.grid(row=3, column=0, sticky='w')
select_level_medium.grid(row=3, column=1, sticky='w')
select_level_high.grid(row=3, column=2, sticky='w')
select_level_extreme.grid(row=3, column=3, sticky='w')

type_label.grid(row=4, column=0, columnspan=4, pady=10)

select_type_AN.grid(row=5, column=0, sticky='w')
select_type_PIN.grid(row=5, column=1, sticky='w')
select_type_PIN6.grid(row=5, column=2, sticky='w')
select_type_ASCII.grid(row=5, column=3, sticky='w')

confirm.grid(row=6, column=0, pady=20)
saves.grid(row=6, column=2, pady=20)

root.mainloop()
