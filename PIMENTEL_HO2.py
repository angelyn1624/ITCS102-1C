import tkinter as tk

window = tk.Tk()
window.title("Angelyn's Profile")
window.geometry("600x600")
window.resizable(True,True)
window.config(bg="pink")

label=tk.Label(window, text ="Student Profile", font=("Arial", 32,"bold"), fg="black", bg="pink", anchor="s")
label.pack(padx=(10),pady=(20))
label=tk.Label(window, text="Name: ANGELYN E. PIMENTEL", font=("Arial", 14,"bold"), fg="black", bg="pink")
label.pack(padx=(10), pady=(10), anchor="w")
label=tk.Label(window, text="\nAge: 23", font=("Arial", 14,"bold"), fg="black", bg="pink")
label.pack(padx=(10), pady=(10), anchor="w")
label=tk.Label(window, text="\nCourse: BSIT 1-C", font=("Arial", 14,"bold"), fg="black", bg="pink")
label.pack(padx=(10), pady=(10), anchor="w")
label=tk.Label(window, text="\nBirthday: June 24, 2002", font=("Arial", 14,"bold"), fg="black", bg="pink")
label.pack(padx=(10), pady=(10), anchor="w")
label=tk.Label(window, text="\nMotto:", font=("Arial", 14,"bold"), fg="black", bg="pink")
label.pack(padx=(10), pady=(10), anchor="w")
label=tk.Label(window, text="No matter what challenges comes into our lives,there is still  hope.", font=("Time New Roman", 14,"italic"), fg="black", bg="pink")
label.pack(padx=(10), pady=(10), anchor="w")

window.mainloop()