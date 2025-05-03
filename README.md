# Google-Translater-Project
📄 Project Title:
Google Translator Application using Python (Tkinter + Googletrans)


🧾 Project Summary:
This project is a graphical user interface (GUI) based language translation tool developed using Python's tkinter library and the googletrans API (version 4.0.0-rc1). It allows users to enter text in one language and translate it into another selected language with a single click. The application supports multiple languages and provides an intuitive interface with dropdowns for selecting source and destination languages, a text box for input, and a translation output display area.

This project demonstrates the integration of third-party APIs in desktop applications and reinforces core Python skills like GUI development, string handling, and external library usage.

⚙️ Functions Used in the Project:
1. change(text, src, dest)
Purpose: Translates the given text from the source language to the destination language.

Parameters:

text: The input string to be translated.

src: The source language (e.g., "english").

dest: The destination language (e.g., "hindi").

Process:

Initializes the Translator() object.

Uses the .translate() method to convert the text.

Returns the translated string.

2. data()
Purpose: Fetches the user's selected languages and input text, performs translation, and displays the output.

Steps:

Gets the selected source language from comb_sor.

Gets the selected destination language from comb_dest.

Fetches the input text from the Sor_txt widget.

Calls the change() function to translate the text.

Deletes any previous output from dest_txt.

Inserts the new translated text into dest_txt.

🖥️ GUI Components Summary:
Component	Purpose
Tk()	Initializes the main application window
Text()	Multi-line text input/output fields
Label()	Displays static text labels
Button()	Triggers translation on click
ttk.Combobox()	Dropdowns for selecting languages
Frame()	Used for layout organization

🧠 Learning Outcomes:
GUI development with Tkinter

Using third-party APIs (googletrans)

Handling user input and output in desktop apps

Error handling and real-time translation

Working with language codes and values
