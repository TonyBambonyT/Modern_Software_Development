import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


def calculate():
    try:
        # Получаем числа из полей ввода как float для поддержки дробных
        n1 = float(entry_1.get())
        n2 = float(entry_2.get())
        oper = combo_oper.get()

        res = ""

        if oper == "+":
            res = n1 + n2
        elif oper == "-":
            res = n1 - n2
        elif oper == "*":
            res = n1 * n2
        elif oper == "/":
            if n2 == 0:
                res = "Ошибка (деление на 0)"
            else:
                res = n1 / n2
        else:
            res = "Выберите операцию"

        lbl_result.configure(text=str(res))

    except ValueError:
        lbl_result.configure(text="Введите числа!")


def show_choice():
    choices = []

    if var1.get() == True:
        choices.append("Первый")
    if var2.get() == True:
        choices.append("Второй")
    if var3.get() == True:
        choices.append("Третий")

    if not choices:
        text = "Вы ничего не выбрали"
    else:
        text = "Вы выбрали: " + ", ".join(choices)

    messagebox.showinfo("Ваш выбор", text)


def open_file():
    file_path = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")))

    if file_path:
        text_area.delete(1.0, tk.END)

        with open(file_path, "r") as f:
            content = f.read()
            text_area.insert(tk.INSERT, content)


window = tk.Tk()
window.title("Тарарыков Антон Алексеевич")
window.geometry("600x400")

main_menu = tk.Menu(window)
window.config(menu=main_menu)

file_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить текст (для вкладки 3)", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=window.quit)

# Создаем вкладки с помощью виджета Notebook
tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Калькулятор')
tab_control.add(tab2, text='Чекбоксы')
tab_control.add(tab3, text='Текст')

tab_control.pack(expand=1, fill='both')

# Вкладка 1: калькулятор; элементы размещены в ряд через grid
entry_1 = tk.Entry(tab1, width=10)
entry_1.grid(column=0, row=0, padx=10, pady=20)

combo_oper = ttk.Combobox(tab1, width=5)
combo_oper['values'] = ('+', '-', '*', '/')
combo_oper.current(0)
combo_oper.grid(column=1, row=0, padx=5)

entry_2 = tk.Entry(tab1, width=10)
entry_2.grid(column=2, row=0, padx=10)

btn_calc = tk.Button(tab1, text="=", command=calculate)
btn_calc.grid(column=3, row=0, padx=5)

lbl_result = tk.Label(tab1, text="Результат")
lbl_result.grid(column=4, row=0, padx=10)

# Вкладка 2: чекбоксы; состояния храним в BooleanVar
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

chk1 = tk.Checkbutton(tab2, text="Первый", variable=var1)
chk1.pack(anchor="w", padx=20, pady=5)

chk2 = tk.Checkbutton(tab2, text="Второй", variable=var2)
chk2.pack(anchor="w", padx=20, pady=5)

chk3 = tk.Checkbutton(tab2, text="Третий", variable=var3)
chk3.pack(anchor="w", padx=20, pady=5)

btn_check = tk.Button(tab2, text="Показать выбор", command=show_choice)
btn_check.pack(padx=20, pady=10)

# Вкладка 3: работа с текстом; используем Text с прокруткой, без ScrolledText
text_area = tk.Text(tab3, width=60, height=20)
text_area.pack(padx=10, pady=10, fill="both", expand=True)

window.mainloop()