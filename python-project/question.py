import tkinter as tk
from tkinter import  ttk


def show_question(self):
        self.clear_screen()
        q_data = self.questions[self.current_q]

        style = ttk.Style()
        style.theme_use("default")
        style.configure("green.Horizontal.TProgressbar", foreground="green", background="green")

        self.progress = ttk.Progressbar(self.root, length=600, mode="determinate",
                                        style="green.Horizontal.TProgressbar")
        self.progress["maximum"] = len(self.questions)
        self.progress["value"] = self.current_q + 1
        self.progress.pack(pady=15)

        tk.Label(self.root, text=f"{self.topic} Quiz",
                 font=("Arial", 16, "bold"),
                 fg="purple").pack(pady=10)

        tk.Label(self.root, text=f"Q{self.current_q + 1}. {q_data['question']}",
                 wraplength=700, justify="left",
                 fg="navy", font=("Arial", 14)).pack(pady=20)

        self.answer_var = tk.StringVar()
        colors = ["#ff9999", "#99ccff", "#99ff99", "#ffcc99"]

        options_frame = tk.Frame(self.root)
        options_frame.pack(pady=30)

        for i, option in enumerate(q_data["options"]):
            row, col = divmod(i, 2)
            tk.Radiobutton(options_frame, text=option, variable=self.answer_var,
                           value=option, font=("Arial", 12),
                           bg=colors[i % len(colors)],
                           indicatoron=0, width=25, pady=10).grid(row=row, column=col, padx=20, pady=15)

        tk.Button(self.root, text="Next", command=self.next_question,
                  font=("Arial", 12, "bold"),
                  bg="orange", fg="white", width=15).pack(pady=40)
