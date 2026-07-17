import tkinter as tk
import tkinter.font as tkfont

def generate_text():
    text = text_entry.get()
    selected_font = font_style_var.get()
    styled_text.delete(1.0, tk.END) 
    styled_text.insert(tk.END, text) 
    styled_text.config(font=(selected_font, 16))  
def copy_text():
    text_to_copy = styled_text.get(1.0, tk.END)  
    root.clipboard_clear()  
    root.clipboard_append(text_to_copy.strip())  
    copy_status_label.config(text="Text copied to clipboard!", fg="green")
root = tk.Tk()
root.title("Text Generator with Font Styles")
instruction_label = tk.Label(root, text="Enter Text and Choose Font Style", font=("Arial", 16))
instruction_label.pack(pady=10)
text_entry = tk.Entry(root, font=("Arial", 14), width=40)
text_entry.pack(pady=10)
font_style_var = tk.StringVar()

font_styles = [
    "Arial", "Courier New", "Times New Roman", "Verdana", "Comic Sans MS", "Georgia", "Tahoma", "Trebuchet MS", "Impact",
    "Lucida Console", "Calibri", "Palatino", "Garamond", "Arial Black", "Comic Sans", "Book Antiqua", "Consolas", "Courier",
    "Futura", "Frank Ruhl", "Lucida Sans", "Optima", "Rockwell", "Serif", "Swiss 721", "Century Gothic",
    "Microsoft Sans Serif", "Lucida Handwriting", "Baskerville", "Brush Script", "Copperplate Gothic", "Didot", "Mistral", "Corbel", "Perpetua",
    "Adobe Garamond", "Algerian", "Andalus", "Ariyal", "Bodoni MT", "Bookman", "Bradley Hand ITC", "Calibri Light", "Chiller", "Comic Sans MS",
    "Consolas", "Copperplate", "Curlz MT", "Droid Sans", "Eras Medium ITC", "Felix Titling", "Franklin Gothic Medium", "Geneva", "Georgia",
    "Gill Sans", "Haettenschweiler", "Harlow Solid Italic", "Harrington", "Helvetica", "Impact", "Lobster", "Lucida Bright", "Monaco", "MS Serif",
    "Noto Sans", "OCR A Extended", "Optima", "Papyrus", "Rockwell Extra Bold", "Segoe UI", "Segoe Print", "Segoe Script", "Source Sans Pro",
    "Tahoma", "Times", "Times New Roman", "Trebuchet MS", "Verdana", "Wingdings", "Arial Rounded MT Bold", "Arial Black", "Brush Script MT",
    "Courier", "FangSong", "SimHei", "SimSun", "Microsoft Sans Serif", "Luminari", "Chalkboard", "Calibri Light", "Calibri", "Tahoma", "Cambria",
    "Constantia", "Corbel", "Corbel Light", "Cochin", "Didot", "Geneva", "Garamond", "Georgia", "Gill Sans", "Lucida Sans Typewriter", "Tahoma",
    "Verdana", "Arial", "Trebuchet MS", "Courier New", "Lucida Console", "Palatino Linotype", "Segoe UI", "Segoe Print", "Segoe Script", "Comic Sans MS",
    "Lucida Calligraphy", "Monotype Corsiva", "Papyrus", "Lucida Sans", "Wingdings 2", "Webdings", "Impact", "Arial Narrow", "Lucida Handwriting",
    "Georgia", "Candara", "Cambria", "Monaco", "Roboto", "Ubuntu", "Tisa", "Lobster", "Pacifico", "Yanone Kaffeesatz", "Raleway", "Lato",
    "Muli", "Roboto Slab", "Bitter", "Open Sans", "PT Sans", "Exo", "Bebas Neue", "Nunito", "Source Sans Pro", "Playfair Display", "PT Serif",
    "Barlow", "Lora", "Quicksand", "Fira Sans", "Zilla Slab", "Overpass", "Rokkitt", "Oxygen", "Quattrocento", "Merriweather", "Tisa Sans",
    "Vollkorn", "Varela Round", "Droid Serif", "Poppins", "Maven Pro", "Hind", "Asap", "Sanchez", "Viga", "Cousine", "Archivo", "Roboto Mono",
    "Muli", "Assistant", "Mukta", "Cabin", "Ubuntu Condensed", "Work Sans", "Zilla Slab", "Libre Baskerville", "Bree Serif", "Crimson Text", "Amatic SC",
    "Anton", "Permanent Marker", "Rock Salt", "Patrick Hand", "Dancing Script", "Tangerine", "Balthazar", "Raleway Dots", "Sacramento", "Playball",
    "Love Ya Like A Sister", "RocknRoll One", "Teko", "Kaushan Script", "Handlee", "Russo One", "Gloria Hallelujah", "Berkshire Swash", "Yesteryear",
    "Tajawal", "Kalam", "Bad Script", "Yellowtail", "Indie Flower", "Fredericka the Great", "Dancing Script", "Caveat", "Bungee", "Indie Flower",
    "Unkempt", "Reenie Beanie", "Lobster Two", "Gloock", "Beth Ellen", "Autour One", "Grand Hotel", "Sacramento", "Dancing Script", "Paytone One",
    "Satisfy", "Balsamiq Sans", "Sunshiney", "Lobster", "Rock Salt", "Anton", "Viga", "Coming Soon", "Julius Sans One", "Allerta", "Averia Serif",
    "Ubuntu", "Corbel", "Arial", "Bebas Neue", "Bitter", "Bungee Inline", "Tangerine", "Hammersmith One", "Courgette", "Rock Salt", "Righteous"
]

font_style_menu = tk.OptionMenu(root, font_style_var, *font_styles)
font_style_menu.pack(pady=10)

font_style_var.set(font_styles[0])  # Set to the first available font

generate_button = tk.Button(root, text="Generate Text", font=("Arial", 14), command=generate_text)
generate_button.pack(pady=10)

styled_text = tk.Text(root, font=("Arial", 14), height=6, width=40, wrap=tk.WORD)
styled_text.pack(pady=10)

copy_button = tk.Button(root, text="Copy Text", font=("Arial", 14), command=copy_text)
copy_button.pack(pady=10)

copy_status_label = tk.Label(root, text="", font=("Arial", 12))
copy_status_label.pack(pady=10)

root.mainloop()
