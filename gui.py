from tkinter import Tk, Label, Button, filedialog
import validator

class SolverGui:
    def __init__(self, master):
        self.master = master
        master.title("Fifteen game solver")

        self.puzzle = None
        self.solution = None

        self.label = Label(master, text="Choose file with puzzle to solve")
        self.label.pack()

        self.greet_button = Button(master, text="Choose file", command=self.open_puzzle)
        self.greet_button.pack()

        self.label2 = Label(master, text="Choose file with solution")
        self.label2.pack()

        self.close_button = Button(master, text="Close", command=self.open_solution)
        self.close_button.pack()

        self.check_button = Button(master, text="Check", command=self.check)
        self.check_button.pack()

    def greet(self):
        print("Greetings!")

    def open_puzzle(self):
        a = filedialog.askopenfilename()
        self.label.config(text=a)
        self.puzzle = validator.load_puzzle(a)

    def open_solution(self):
        a = filedialog.askopenfilename()
        self.label2.config(text=a)
        self.solution = validator.load_solution(a)

    def check(self):
        if self.puzzle is not None and self.solution is not None:
            valid = validator.Game(self.puzzle)
            valid.solve(self.puzzle)


root = Tk()
my_gui = SolverGui(root)
root.mainloop()