from tkinter.filedialog import askopenfilename
from tkinter import Tk

file = None
msgs = None
messages = []


def read_file():
    root = Tk()
    root.withdraw()
    file = askopenfilename(
        title="Выберите текстовый файл",
        filetypes=[("Текстовый файл", "*.txt")]
    )
    root.destroy()
    return file


def main():
    file = read_file()
    new_file = file.split(".")[0] + "_готовая_переписка.txt"

    with open(file, "r", encoding="utf-8") as f:
        msgs = f.read().split("\n\n")
        messages.append(i.split("\n")[0] for i in msgs)

    with open(new_file, "a", encoding="utf-8") as f:
        for i in msgs:
            f.write(f"- {i.split("\n")[1]}\n")
    print(f"Файл {new_file} создан!")
    

if __name__ == "__main__":
    main()