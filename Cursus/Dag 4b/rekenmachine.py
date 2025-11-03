import customtkinter as ctk


root = ctk.CTk()
root.geometry()  # width x height + x_offset + y_offset

w = ctk.CTkLabel(root, text="Rekenmachine", font=ctk.CTkFont(size=30))
w.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

w = ctk.CTkLabel(root, text="Getal 1")
w.grid(row=1, column=0, padx=20, pady=10)

getal1_var = ctk.StringVar()
getal1_widget = ctk.CTkEntry(root, textvariable=getal1_var)
getal1_widget.grid(row=1, column=1, padx=20, pady=10)

w = ctk.CTkLabel(root, text="Getal 2")
w.grid(row=2, column=0, padx=20, pady=10)

getal2_var = ctk.StringVar()
getal2_widget = ctk.CTkEntry(root, textvariable=getal2_var)
getal2_widget.grid(row=2, column=1, padx=20, pady=10)

def add_button_click_handler():
    getal1 = int(getal1_var.get())
    getal2 = int(getal2_var.get())
    uitkomst = getal1 + getal2
    uitkomst_var.set(str(uitkomst))

w = ctk.CTkButton(root, text="optellen", command=add_button_click_handler)
w.grid(row=3, column=0, padx=20, pady=10)

def multiply_button_click_handler():
    getal1 = int(getal1_var.get())
    getal2 = int(getal2_var.get())
    uitkomst = getal1 * getal2
    uitkomst_var.set(str(uitkomst))

w = ctk.CTkButton(root, text="vermenigvuldigen", command=multiply_button_click_handler)
w.grid(row=3, column=1, padx=20, pady=10)

w = ctk.CTkLabel(root, text="Uitkomst")
w.grid(row=4, column=0, padx=20, pady=10)

uitkomst_var = ctk.StringVar()
uitkomst_widget = ctk.CTkEntry(root, textvariable=uitkomst_var)
uitkomst_widget.grid(row=4, column=1, padx=20, pady=10)


root.mainloop()


