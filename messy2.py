# Messy Code
class EmailValidator:
    def __init__(self, email):
        self.email = email

    def validate_email(self):
        if "@" not in self.email:
            return False
        return True

    def send_email(self, message):
        print(f"Sending email to {self.email}: {message}")

    def save_email_to_database(self):
        print(f"Saving {self.email} to the database.")

# Example usage:
email = EmailValidator("user@example.com")
if email.validate_email():
    email.send_email("Welcome!")
    email.save_email_to_database()
