import json

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