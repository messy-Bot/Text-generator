import tkinter as tk


# Core function used by the application and automated tests
def generate_styled_text(text, font_name):
    return {
        "text": text,
        "font": font_name,
        "size": 16
    }


def create_gui():
    root = tk.Tk()
    root.title("Text Generator with Font Styles")
    root.geometry("600x650")

    # Instruction
    instruction_label = tk.Label(
        root,
        text="Enter Text and Choose Font Style",
        font=("Arial", 16)
    )
    instruction_label.pack(pady=10)

    # Text input
    text_entry = tk.Entry(
        root,
        font=("Arial", 14),
        width=40
    )
    text_entry.pack(pady=10)

    # Font selection
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
        "Pacifico"
    ]

    font_style_menu = tk.OptionMenu(
        root,
        font_style_var,
        *font_styles
    )
    font_style_menu.pack(pady=10)

    font_style_var.set(font_styles[0])

    # Output text area
    styled_text = tk.Text(
        root,
        font=("Arial", 14),
        height=6,
        width=40,
        wrap=tk.WORD
    )
    styled_text.pack(pady=10)

    # Status label
    copy_status_label = tk.Label(
        root,
        text="",
        font=("Arial", 12)
    )
    copy_status_label.pack(pady=10)

    # Generate text
    def generate_text():
        text = text_entry.get()
        selected_font = font_style_var.get()

        result = generate_styled_text(
            text,
            selected_font
        )

        styled_text.delete("1.0", tk.END)
        styled_text.insert(tk.END, result["text"])

        styled_text.config(
            font=(result["font"], result["size"])
        )

    # Copy text
    def copy_text():
        text_to_copy = styled_text.get(
            "1.0",
            tk.END
        )

        root.clipboard_clear()
        root.clipboard_append(
            text_to_copy.strip()
        )

        copy_status_label.config(
            text="Text copied to clipboard!",
            fg="green"
        )

    # Generate button
    generate_button = tk.Button(
        root,
        text="Generate Text",
        font=("Arial", 14),
        command=generate_text
    )
    generate_button.pack(pady=10)

    # Copy button
    copy_button = tk.Button(
        root,
        text="Copy Text",
        font=("Arial", 14),
        command=copy_text
    )
    copy_button.pack(pady=10)

    root.mainloop()


# Start GUI only when this file is run directly.
# This prevents pytest from opening the Tkinter window.
if __name__ == "__main__":
    create_gui()
