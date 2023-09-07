import os
import tkinter as tk
from tkinter import filedialog
import random
import string


def generate_noise():
    basic_confusers = [
        '::REM Did you hear about the programmer who had a bad cold? He had a terminal illness!',
        '::REM Why did the computer catch a cold? It left its Windows open!',
        '::REM I told my computer I needed a break, but it just gave me a coffee error.',
        '::REM This code is like a dad joke in binary: 01001001 00100111 01101101 00100000 01110011 01101111 00100000 01110010 01110101 01101110 01101110 01111001!',
        '::REM Warning! Unauthorized access detected. Just kidding, its just a skid trying to be cool!',
        '::REM Why did the skid become a programmer? Because he wanted to be a kid forever!',
        '::REM Every kid hacker starts somewhere... usually in this mess of code!',
        '::REM This code is so old, even skids would call it vintage.',
        '::REM Remember the first time you tried to hack? Thats the level of this code!',
        '::REM If I had a penny for every kid who tried to understand this code... Id have like, 3 pennies!',
        '::REM Dont be a skid, be a squid. At least they swim fast!',
        '::REM Someone told me skids have the best playground - a sandbox!',
        '::REM Hey skid, dont touch this code! You might accidentally improve it!',
        '::REM Someone said this code is kid-proof. The skid community disagreed!',
        '::REM Skids be like: Im a hacker! But cant even navigate this code maze.',
        '::REM Hey kid, looking for some hacks? You wont find any here... just more bad jokes!',
        '::REM To the skid trying to decipher this: Good luck! Youll need it!',
        '::REM Is it a bird? Is it a plane? Nope, just another skid flying through the code!',
        '::REM If skidding was an Olympic sport, youd be looking at the training grounds right now!',
        '::REM Whats a skids favorite coding language? PlaygroundScript!',
        '::REM Knock knock. Whos there? Skid. Skid who? Skid you not, this code is a mess!'
    ]
    special_confusers = ['::REM ' + ''.join(random.choices(string.ascii_letters + string.digits, k=50)) for _ in
                         range(50)] + \
                        ['::REM NOP'] * 50 + \
                        ['::REM ' + ''.join(random.choices("가나다라마바사아자차카타파하", k=10)) for _ in range(50)]

    confusers = basic_confusers + special_confusers
    random.shuffle(confusers)

    return random.choices(confusers, k=20) + ['::REM NOP'] * 50


def confuse_content(content):
    lines = content.split('\n')
    confused_content = []

    confused_content.extend(lines[:2])
    non_latin_counter = 0

    for line in lines[2:]:
        confused_content.append(line)
        confused_content.extend(generate_noise())

    return '\n'.join(confused_content)


def create_confused_batch(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as input_file:
            batch_content = input_file.read()

        confused_content = confuse_content(batch_content)

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
