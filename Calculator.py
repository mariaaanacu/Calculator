import tkinter as tk

class CalculatorApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Calculator")
        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self.master, width=30, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.button_1 = tk.Button(self.master, text="1", padx=40, pady=20, command=lambda: self.button_click(1))
        self.button_2 = tk.Button(self.master, text="2", padx=40, pady=20, command=lambda: self.button_click(2))
        self.button_3 = tk.Button(self.master, text="3", padx=40, pady=20, command=lambda: self.button_click(3))
        self.button_4 = tk.Button(self.master, text="4", padx=40, pady=20, command=lambda: self.button_click(4))
        self.button_5 = tk.Button(self.master, text="5", padx=40, pady=20, command=lambda: self.button_click(5))
        self.button_6 = tk.Button(self.master, text="6", padx=40, pady=20, command=lambda: self.button_click(6))
        self.button_7 = tk.Button(self.master, text="7", padx=40, pady=20, command=lambda: self.button_click(7))
        self.button_8 = tk.Button(self.master, text="8", padx=40, pady=20, command=lambda: self.button_click(8))
        self.button_9 = tk.Button(self.master, text="9", padx=40, pady=20, command=lambda: self.button_click(9))
        self.button_0 = tk.Button(self.master, text="0", padx=40, pady=20, command=lambda: self.button_click(0))
        self.button_add = tk.Button(self.master, text="+", padx=39, pady=20, command=self.button_add)
        self.button_equal = tk.Button(self.master, text="=", padx=91, pady=20, command=self.button_equal)
        self.button_clear = tk.Button(self.master, text="Clear", padx=79, pady=20, command=self.button_clear)

        # Plasarea butoanelor pe grila
        self.button_1.grid(row=3, column=0)
        self.button_2.grid(row=3, column=1)
        self.button_3.grid(row=3, column=2)

        self.button_4.grid(row=2, column=0)
        self.button_5.grid(row=2, column=1)
        self.button_6.grid(row=2, column=2)

        self.button_7.grid(row=1, column=0)
        self.button_8.grid(row=1, column=1)
        self.button_9.grid(row=1, column=2)

        self.button_0.grid(row=4, column=0)
        self.button_clear.grid(row=4, column=1, columnspan=2)
        self.button_add.grid(row=5, column=1)
        self.button_equal.grid(row=5, column=0, columnspan=2)
        self.button_subtract = tk.Button(self.master, text="-", padx=41, pady=20, command=self.button_subtract)
        self.button_multiply = tk.Button(self.master, text="*", padx=40, pady=20, command=self.button_multiply)
        self.button_divide = tk.Button(self.master, text="/", padx=41, pady=20, command=self.button_divide)

        self.button_subtract.grid(row=6, column=0)
        self.button_multiply.grid(row=6, column=1)
        self.button_divide.grid(row=6, column=2)

    def button_click(self, number):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(current) + str(number))

    def button_clear(self):
        self.entry.delete(0, tk.END)

    def button_add(self):
        first_number = self.entry.get()
        global f_num
        global math_operation
        math_operation = "addition"
        f_num = int(first_number)
        self.entry.delete(0, tk.END)

    def button_subtract(self):
        first_number = self.entry.get()
        global f_num
        global math_operation
        math_operation = "subtraction"
        f_num = int(first_number)
        self.entry.delete(0, tk.END)

    def button_multiply(self):
        first_number = self.entry.get()
        global f_num
        global math_operation
        math_operation = "multiplication"
        f_num = int(first_number)
        self.entry.delete(0, tk.END)

    def button_divide(self):
        first_number = self.entry.get()
        global f_num
        global math_operation
        math_operation = "division"
        f_num = int(first_number)
        self.entry.delete(0, tk.END)

    def button_equal(self):
        second_number = self.entry.get()
        self.entry.delete(0, tk.END)

        if math_operation == "addition":
            self.entry.insert(0, f_num + int(second_number))
        elif math_operation == "subtraction":
            self.entry.insert(0, f_num - int(second_number))
        elif math_operation == "multiplication":
            self.entry.insert(0, f_num * int(second_number))
        elif math_operation == "division":
            self.entry.insert(0, f_num / int(second_number))


root = tk.Tk()
app = CalculatorApp(master=root)
app.mainloop()