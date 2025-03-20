class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    def save(self, user):
        print(f"Saving user {user.name} to the database.")

class EmailService:
    def send_welcome_email(self, user):
        print(f"Sending welcome email to {user.email}.")
# -------------------------------------------------------------------------
user = User("Alice", "alice@example.com")
repo = UserRepository()
email_service = EmailService()

repo.save(user)
email_service.send_welcome_email(user)
