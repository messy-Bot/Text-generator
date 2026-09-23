import tkinter as tk


def generate_text():
    text = text_entry.get()
    selected_font = font_style_var.get()

    styled_text.delete("1.0", tk.END)
    styled_text.insert(tk.END, text)
    styled_text.config(font=(selected_font, 16))


def copy_text():
    text_to_copy = styled_text.get("1.0", tk.END)

    root.clipboard_clear()
    root.clipboard_append(text_to_copy.strip())
    copy_status_label.config(
        text="Text copied to clipboard!",
        fg="green"
    )


root = tk.Tk()
root.title("Text Generator with Font Styles")

instruction_label = tk.Label(
    root,
    text="Enter Text and Choose Font Style",
    font=("Arial", 16)
)
instruction_label.pack(pady=10)

text_entry = tk.Entry(root, font=("Arial", 14), width=40)
text_entry.pack(pady=10)

font_style_var = tk.StringVar()

font_styles = [
    "Arial",
    "Courier New",
    "Times New Roman",
    "Verdana",
    "Comic Sans MS",
    "Georgia",
    "Tahoma",
    "Trebuchet MS",
    "Impact",
    "Lucida Console",
    "Calibri",
    "Palatino",
    "Garamond",
    "Arial Black",
    "Consolas",
    "Helvetica",
    "Segoe UI",
    "Roboto",
    "Ubuntu",
    "Lato",
    "Open Sans",
    "Poppins",
    "Playfair Display",
    "Merriweather",
    "Dancing Script",
    "Lobster",
    "Pacifico",
]

font_style_menu = tk.OptionMenu(
    root,
    font_style_var,
    *font_styles
)
font_style_menu.pack(pady=10)

font_style_var.set(font_styles[0])

generate_button = tk.Button(
    root,
    text="Generate Text",
    font=("Arial", 14),
    command=generate_text
)
generate_button.pack(pady=10)

styled_text = tk.Text(
    root,
    font=("Arial", 14),
    height=6,
    width=40,
    wrap=tk.WORD
)
styled_text.pack(pady=10)

copy_button = tk.Button(
    root,
    text="Copy Text",
    font=("Arial", 14),
    command=copy_text
)
copy_button.pack(pady=10)

copy_status_label = tk.Label(
    root,
    text="",
    font=("Arial", 12)
)
copy_status_label.pack(pady=10)

root.mainloop()
