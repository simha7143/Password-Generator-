root.resizable(False, False)

title = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"))
title.pack(pady=10)

length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root, width=10)
length_entry.pack(pady=5)

# Options for character types
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_special = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_upper).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lower).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Numbers", variable=var_digits).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Special Characters", variable=var_special).pack(anchor='w', padx=20)

generate_btn = tk.Button(root, text="Generate Password", command=generate_password, bg="lightblue")
generate_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=350)
result_label.pack(pady=10)

root.mainloop()
