import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")
        
        self.expression = ""
        self.input_text = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Display frame
        display_frame = tk.Frame(self.root, bg="#1e1e1e", height=100)
        display_frame.pack(fill="both", pady=20, padx=20)
        
        # Display entry
        display = tk.Entry(
            display_frame,
            textvariable=self.input_text,
            font=("Arial", 28, "bold"),
            bg="#2d2d2d",
            fg="#ffffff",
            bd=0,
            justify="right",
            relief="flat"
        )
        display.pack(fill="both", expand=True, ipady=20, ipadx=10)
        
        # Buttons frame
        buttons_frame = tk.Frame(self.root, bg="#1e1e1e")
        buttons_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Button layout
        buttons = [
            ['C', '/', '*', '←'],
            ['7', '8', '9', '-'],
            ['4', '5', '6', '+'],
            ['1', '2', '3', '='],
            ['0', '.', '', '']
        ]
        
        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                if btn_text:
                    if btn_text == '=':
                        btn = tk.Button(
                            buttons_frame,
                            text=btn_text,
                            command=self.calculate,
                            bg="#4CAF50",
                            fg="#ffffff",
                            font=("Arial", 18, "bold"),
                            bd=0,
                            cursor="hand2",
                            activebackground="#45a049"
                        )
                        btn.grid(row=i, column=j, rowspan=1, columnspan=1, sticky="nsew", padx=3, pady=3)
                    elif btn_text in ['C', '←']:
                        btn = tk.Button(
                            buttons_frame,
                            text=btn_text,
                            command=lambda x=btn_text: self.clear() if x == 'C' else self.backspace(),
                            bg="#FF5252",
                            fg="#ffffff",
                            font=("Arial", 18, "bold"),
                            bd=0,
                            cursor="hand2",
                            activebackground="#e04848"
                        )
                        btn.grid(row=i, column=j, sticky="nsew", padx=3, pady=3)
                    elif btn_text in ['/', '*', '-', '+']:
                        btn = tk.Button(
                            buttons_frame,
                            text=btn_text,
                            command=lambda x=btn_text: self.append_operator(x),
                            bg="#FF9800",
                            fg="#ffffff",
                            font=("Arial", 18, "bold"),
                            bd=0,
                            cursor="hand2",
                            activebackground="#e68900"
                        )
                        btn.grid(row=i, column=j, sticky="nsew", padx=3, pady=3)
                    else:
                        if btn_text == '0':
                            btn = tk.Button(
                                buttons_frame,
                                text=btn_text,
                                command=lambda x=btn_text: self.append_number(x),
                                bg="#424242",
                                fg="#ffffff",
                                font=("Arial", 18, "bold"),
                                bd=0,
                                cursor="hand2",
                                activebackground="#333333"
                            )
                            btn.grid(row=i, column=j, columnspan=2, sticky="nsew", padx=3, pady=3)
                        else:
                            btn = tk.Button(
                                buttons_frame,
                                text=btn_text,
                                command=lambda x=btn_text: self.append_number(x),
                                bg="#424242",
                                fg="#ffffff",
                                font=("Arial", 18, "bold"),
                                bd=0,
                                cursor="hand2",
                                activebackground="#333333"
                            )
                            btn.grid(row=i, column=j, sticky="nsew", padx=3, pady=3)
        
        # Configure grid weights for responsive layout
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
    
    def append_number(self, number):
        self.expression += str(number)
        self.input_text.set(self.expression)
    
    def append_operator(self, operator):
        if self.expression and self.expression[-1] not in ['+', '-', '*', '/']:
            self.expression += operator
            self.input_text.set(self.expression)
    
    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except ZeroDivisionError:
            self.input_text.set("Error: Division by zero")
            self.expression = ""
        except:
            self.input_text.set("Error")
            self.expression = ""
    
    def clear(self):
        self.expression = ""
        self.input_text.set("")
    
    def backspace(self):
        self.expression = self.expression[:-1]
        self.input_text.set(self.expression)

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
