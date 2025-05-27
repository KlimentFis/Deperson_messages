from tkinter.filedialog import askopenfilename
from tkinter import Tk

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
    if not file:
        print("Файл не выбран!")
        return
    new_file = file.split(".")[0] + "_готовая_переписка.txt"

    with open(file, "r", encoding="utf-8") as f:
        msgs = f.read().split("\n\n")

    # Обрабатываем сообщения: определяем отправителя и склеиваем подряд идущие реплики одного человека
    messages = []
    current_sender = None
    current_content = ""
    for msg in msgs:
        lines = msg.strip().split("\n")
        if len(lines) < 2:
            continue
        sender_line = lines[0]
        # Определяем имя отправителя (до первой запятой)
        sender = sender_line.split(",")[0].strip()
        content = "\n".join(line.strip() for line in lines[1:]).strip()
        if sender == current_sender:
            # Склеиваем с предыдущей репликой
            current_content += "\n" + content if current_content else content
        else:
            # Добавляем предыдущее сообщение в список
            if current_sender is not None:
                messages.append(current_content)
            current_sender = sender
            current_content = content
    # Добавляем последнее сообщение
    if current_sender is not None:
        messages.append(current_content)

    with open(new_file, "w", encoding="utf-8") as f:
        for msg in messages:
            f.write(f"- {msg}\n")
    print(f"Файл {new_file} создан!")

if __name__ == "__main__":
    main()
