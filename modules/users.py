import json
import os

class UserManager:
    def __init__(self, config, logger):
        self.file_path = config['data_paths']['users']
        self.logger = logger
        self.users = self.load_users()

    def load_users(self):
        if not os.path.exists(self.file_path):
            return {}
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def save_users(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.users, f, indent=4)

    def add_user(self):
        username = input("Enter username: ")
        role = input("Enter role (admin/staff): ")
        self.users[username] = {'role': role}
        self.save_users()
        self.logger.info(f"User {username} added with role {role}.")