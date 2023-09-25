import os
import tkinter as tk
from tkinter import filedialog
import random
import string


def generate_noise():
    junk_codes = [
        f'set {"".join(random.choices(string.ascii_lowercase, k=5))}=%random%^',
        f'if not "%random%"=="%random%" echo This will never execute^',
        f'for %%i in (A B C D E F G H I J K) do echo %random%^'
    ]
    return '^'.join(random.choices(junk_codes, k=1500))  # 30 vezes mais Junk Codes, em uma única linha.


def confuse_content():
    return generate_noise()


def create_confused_batch(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as input_file:
            _ = input_file.read()

        confused_content = confuse_content()

        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(confused_content)

        return f"File successfully confounded as {output_path}"

    except Exception as e:
        return f"Error confounding the file: {str(e)}"


def browse_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("Batch Files", "*.bat")])
    entry_input_file.delete(0, tk.END)
    entry_input_file.insert(0, file_path)


def browse_output_directory():
    directory_path = filedialog.askdirectory()
    if directory_path:
        entry_output_name.delete(0, tk.END)
        entry_output_name.insert(0, os.path.join(directory_path, "output-Confounded.bat"))


def confuse():
    input_file = entry_input_file.get()
    output_path = entry_output_name.get()

    if input_file and output_path:
        result = create_confused_batch(input_file, output_path)
        label_result.config(text=result)
    else:
        label_result.config(text="Please select an input file and define an output path.")


window = tk.Tk()
window.title("Black man Confuser")

label_input_file = tk.Label(window, text="Select the input .bat file:")
label_input_file.pack()

entry_input_file = tk.Entry(window, width=50)
entry_input_file.pack()

button_browse_input = tk.Button(window, text="Browse", command=browse_input_file)
button_browse_input.pack()

label_output_name = tk.Label(window, text="Output file path:")
label_output_name.pack()

entry_output_name = tk.Entry(window, width=50)
entry_output_name.pack()

button_browse_output = tk.Button(window, text="Select Directory", command=browse_output_directory)
button_browse_output.pack()

button_confuse = tk.Button(window, text="Confound", command=confuse)
button_confuse.pack()

label_result = tk.Label(window, text="")
label_result.pack()

window.mainloop()
