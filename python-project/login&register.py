import tkinter as tk
from tkinter import messagebox
import json 

 #  Login/Register 
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