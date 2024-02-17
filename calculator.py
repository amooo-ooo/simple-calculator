import tkinter as tk
from math import sqrt, pi, sin, cos, tan, sinh, cosh, tanh, asinh, acosh, atanh, e, inf, tau
from functools import partial

class MainWindow(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Calculator")
        self.error = False
        self.default = ["CE","1/x","(",")","pi", "abs", "sqrt","/", "7", "8", "9", "*", "4", "5", "6", "-", "1", "2", "3", "+", "+/-", "0", ".", "="]
    
        self.value = ""
        self.labelVar = tk.StringVar()

        dropdowns = self._dropdowns()
        dropdowns.pack()

        display = self._display()
        display.pack(pady=14)

        buttons = self._buttons()
        buttons.pack()
        self.resizable(False, False)

    def _dropdowns(self) -> tk.Frame:
        div = tk.Frame(master=self)
        edit = tk.Button(master=div, text="TRIG", command=partial(self._dropdown, ["sin", "cos", "tan","sinh", "cosh","tanh", "asinh","acosh","atanh"], "TRIG"), width=5, font=("Helvetica", 10), anchor="w", bd=0)
        cons = tk.Button(master=div, text="CONS", command=partial(self._dropdown, ["e","inf","tau"], "CONS"), width=29, font=("Helvetica", 10), anchor="w", bd=0)
        edit.grid(row=0, column=0)
        cons.grid(row=0, column=1)

        return div

    def _display(self) -> tk.Label:
        div = tk.Label(master=self, textvariable=self.labelVar, font=("Helvetica", 30), anchor="e", width=12)
        return div
        
    def _buttons(self) -> tk.Frame:
        div = tk.Frame(master=self)
        limit = 4
        for index, value in enumerate(self.default):
            if value == "=": run = self._calculate
            elif value == "CE": run = self._clear
            elif value == "1/x": run = partial(self._calculate, "1/")
            elif value == "+/-": run = partial(self._calculate, "-")
            else: run = partial(self._update_value, value)
            
            button = tk.Button(text=value, master=div, width=6, height=2, command=run, font=("Helvetica", 14), bd=1)
            x, y = divmod(index, limit)
            button.grid(row=x, column=y)
            
        return div

    def _dropdown_buttons(self, options: list, master: tk.Tk) -> tk.Frame:
        div = tk.Frame(master=master)
        limit = 3
        for index, value in enumerate(options):
            button = tk.Button(text=value, command=partial(self._update_value, value), master=div, width=6, height=2, font=("Helvetica", 14), bd=1)
            x, y = divmod(index, limit)
            button.grid(row=x, column=y)
            
        return div

    def _dropdown(self, options, title):
        dropdown = tk.Tk()
        dropdown.title(title)

        buttons = self._dropdown_buttons(options, master=dropdown)
        buttons.pack()
    
        dropdown.mainloop()

    def _update_value(self, value) -> None:
        self.value += value
        self.labelVar.set(self.value)

    def _clear(self) -> None:
        self.value = self.value if self.error else ""
        self.labelVar.set(self.value)
        if self.error: self.error = False

    def _calculate(self, add: str = "") -> None:
        try:
            self.value = str(eval(add + self.value))
            self.labelVar.set(self.value)
        except:
            self.error = True
            self.labelVar.set("ERROR")

def main():
    calculator = MainWindow()
    calculator.mainloop()

if __name__ == "__main__":
    main()
