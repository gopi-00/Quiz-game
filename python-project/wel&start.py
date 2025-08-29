import tkinter as tk
from quiz_data import quiz_data

def show_start_screen(self):
        self.clear_screen()
        frame = tk.Frame(self.root)
        frame.pack(expand=True)

        tk.Label(frame, text=f"🎉 Welcome {self.player_name}! 🎉",
                 font=("Arial", 26, "bold"),
                 fg="darkblue").pack(pady=20)

        tk.Label(frame, text="Choose a topic:", font=("Arial", 12)).pack(pady=5)
        self.topic_var = tk.StringVar(value=list(quiz_data.keys())[0])
        tk.OptionMenu(frame, self.topic_var, *quiz_data.keys()).pack()

        tk.Button(frame, text="Start Quiz", command=self.start_quiz,
                  font=("Arial", 12, "bold"),
                  bg="green", fg="white", width=12).pack(pady=20)

        tk.Button(frame, text="Logout", command=self.show_login_screen,
                  font=("Arial", 12, "bold"),
                  bg="red", fg="white", width=12).pack(pady=10)

def start_quiz(self):
        self.topic = self.topic_var.get()
        self.questions = quiz_data[self.topic]
        self.current_q = 0
        self.score = 0
        self.show_question()