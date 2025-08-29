
import tkinter as tk
import json

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
