 
from tkinter import messagebox

def next_question(self):
        selected = self.answer_var.get()
        if selected == "":
            messagebox.showwarning("No Selection", "Please select an answer!")
            return

        if selected == self.questions[self.current_q]["answer"]:
            self.score += 1

        self.current_q += 1
        if self.current_q < len(self.questions):
            self.show_question()
        else:
            self.show_result()