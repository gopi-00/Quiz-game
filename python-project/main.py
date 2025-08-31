import tkinter as tk
from tkinter import messagebox, ttk
from quiz_data import quiz_data
import json 


class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Colorful Quiz Game")
        self.root.geometry("800x600")

        # Quiz attributes
        self.player_name = ""
        self.topic = ""
        self.questions = []
        self.current_q = 0
        self.score = 0

        # User data file
        self.users_file = "users.json"
        try:
            with open(self.users_file, "r") as f:
                self.users = json.load(f)
        except:
            self.users = {}

        # Start with login screen
        self.show_login_screen()

    # ------------------ Utility ------------------
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # ------------------ Login/Register ------------------
    def show_login_screen(self):
        self.clear_screen()
        frame = tk.Frame(self.root)
        frame.pack(expand=True)

        tk.Label(frame, text="🔐 Quiz Game Login",
                 font=("Arial", 24, "bold"), fg="darkblue").pack(pady=20)

        tk.Label(frame, text="Username:", font=("Arial", 12)).pack()
        self.username_entry = tk.Entry(frame, font=("Arial", 12))
        self.username_entry.pack(pady=5)

        tk.Label(frame, text="Password:", font=("Arial", 12)).pack()
        self.password_entry = tk.Entry(frame, font=("Arial", 12), show="*")
        self.password_entry.pack(pady=5)

        tk.Button(frame, text="Login", command=self.login,
                  font=("Arial", 12, "bold"), bg="green", fg="white", width=12).pack(pady=10)
        tk.Button(frame, text="Register", command=self.show_register_screen,
                  font=("Arial", 12, "bold"), bg="blue", fg="white", width=12).pack(pady=5)

    def show_register_screen(self):
        self.clear_screen()
        frame = tk.Frame(self.root)
        frame.pack(expand=True)

        tk.Label(frame, text="📝 Register New Player",
                 font=("Arial", 24, "bold"), fg="purple").pack(pady=20)

        tk.Label(frame, text="Choose Username:", font=("Arial", 12)).pack()
        self.reg_username = tk.Entry(frame, font=("Arial", 12))
        self.reg_username.pack(pady=5)

        tk.Label(frame, text="Choose Password:", font=("Arial", 12)).pack()
        self.reg_password = tk.Entry(frame, font=("Arial", 12), show="*")
        self.reg_password.pack(pady=5)

        tk.Button(frame, text="Register", command=self.register_user,
                  font=("Arial", 12, "bold"), bg="orange", fg="white", width=12).pack(pady=20)
        tk.Button(frame, text="Back to Login", command=self.show_login_screen,
                  font=("Arial", 12, "bold"), bg="gray", fg="white", width=12).pack()

    def register_user(self):
        username = self.reg_username.get().strip()
        password = self.reg_password.get().strip()

        if username in self.users:
            messagebox.showwarning("Error", "Username already exists!")
            return

        if username == "" or password == "":
            messagebox.showwarning("Error", "Please fill all fields!")
            return

        self.users[username] = {"password": password, "scores": []}
        with open(self.users_file, "w") as f:
            json.dump(self.users, f)

        messagebox.showinfo("Success", "Registration successful! Please login.")
        self.show_login_screen()

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if username not in self.users or self.users[username]["password"] != password:
            messagebox.showerror("Login Failed", "Invalid username or password!")
            return

        self.player_name = username
        self.show_start_screen()
        
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
    

        all_questions = quiz_data[self.topic]
    
  
        num_questions = min(5, len(all_questions))
        self.questions = random.sample(all_questions, num_questions)
    
        self.current_q = 0
        self.score = 0
        self.show_question()
        
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

    def show_result(self):
        self.clear_screen()

        # Save score for this user
        self.users[self.player_name]["scores"].append(
            {"topic": self.topic, "score": self.score}
        )
        with open(self.users_file, "w") as f:
            json.dump(self.users, f)

        frame = tk.Frame(self.root)
        frame.pack(expand=True)

        tk.Label(frame, text="🎊 Quiz Completed! 🎊",
                 font=("Arial", 20, "bold"),
                 fg="darkgreen").pack(pady=20)

        tk.Label(frame, text=f"Player: {self.player_name}",
                 font=("Arial", 14)).pack(pady=5)

        tk.Label(frame, text=f"Score: {self.score}/{len(self.questions)}",
                 font=("Arial", 16, "bold"),
                 fg="red").pack(pady=15)

        tk.Label(frame, text="🏆 Your Past Scores 🏆",
                 font=("Arial", 14, "bold"), fg="blue").pack(pady=10)

        # Display last 10 scores for this user
        for record in reversed(self.users[self.player_name]["scores"][-10:]):
            tk.Label(frame, text=f"{record['topic']} - {record['score']}",
                     font=("Arial", 12)).pack()

        tk.Button(frame, text="Play Again", command=self.show_start_screen,
                  font=("Arial", 12, "bold"),
                  bg="blue", fg="white", width=12).pack(pady=10)

        tk.Button(frame, text="Logout", command=self.show_login_screen,
                  font=("Arial", 12, "bold"),
                  bg="gray", fg="white", width=12).pack(pady=5)

        tk.Button(frame, text="Exit", command=self.root.quit,
                  font=("Arial", 12, "bold"),
                  bg="black", fg="white", width=12).pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    QuizGame(root)
    root.mainloop()

