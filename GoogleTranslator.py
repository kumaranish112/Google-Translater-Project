from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", src="english", dest="hindi"):
    translator = Translator()
    translation = translator.translate(text, src=src.lower(), dest=dest.lower())
    return translation.text

def data():
    src_lang = comb_sor.get()
    dest_lang = comb_dest.get()
    input_text = Sor_txt.get(1.0, END)
    try:
        translated_text = change(text=input_text, src=src_lang, dest=dest_lang)
        dest_txt.delete(1.0, END)
        dest_txt.insert(END, translated_text)
    except Exception as e:
        dest_txt.delete(1.0, END)
        dest_txt.insert(END, f"Error: {str(e)}")

root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='red')

Label(root, text="Translator", font=("Times New Roman", 40, "bold")).place(x=100, y=40, height=50, width=300)

Label(root, text="Source Text", font=("Times New Roman", 20, "bold"), fg="Black", bg="red").place(x=100, y=100, height=20, width=300)

frame = Frame(root)
frame.pack(side=BOTTOM)

Sor_txt = Text(root, font=("Times New Roman", 20, "bold"), wrap=WORD)
Sor_txt.place(x=10, y=130, height=150, width=480)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(root, value=list_text)
comb_sor.place(x=10, y=300, height=40, width=150)
comb_sor.set("english")

Button(root, text="Translate", relief=RAISED, command=data).place(x=170, y=300, height=40, width=150)

comb_dest = ttk.Combobox(root, value=list_text)
comb_dest.place(x=330, y=300, height=40, width=105)
comb_dest.set("hindi")

Label(root, text="Dest Text", font=("Times New Roman", 20, "bold"), fg="Black", bg="red").place(x=100, y=360, height=20, width=300)

dest_txt = Text(root, font=("Times New Roman", 20, "bold"), wrap=WORD)
dest_txt.place(x=10, y=400, height=150, width=480)

root.mainloop()
