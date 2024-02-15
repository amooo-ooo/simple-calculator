import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Calculator")
        self.value = ""

        display = self._display()
        display.pack()

        buttons = self._buttons()
        buttons.pack()

    def _display(self) -> tk.Label:
        div = tk.Label(master=self, textvariable=self.value)
        return div
        

    def _buttons(self) -> tk.Frame:
        buttons = ["7","8","9","*","4","5","6","-","1","2","3","+",".","0","","/"]
        div = tk.Frame(master=self)
        limit = 4
        for index, value in enumerate(buttons):
            button = tk.Button(text=value, master=div, width=10, height=5, command=lambda: value)
            x, y = divmod(index, limit)
            button.grid(row=x, column=y)
        return div

    def _update_value(value) -> None:
        self.value += value
        labelVar.set(newValue)
            
            

def main():
    calculator = MainWindow()
    calculator.mainloop()
    

if __name__ == "__main__":
    main()
