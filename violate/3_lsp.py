#  LSP Violation: User and AdminUser
class User:
    def create_post(self, content):
        print(f"Creating post: {content}")

class StandardUser(User):
    def create_post(self, content):
        # Standard users can create posts normally
        super().create_post(content)

class AdminUser(User):
    def create_post(self, content):
        if not self.verify_content(content):
            raise ValueError("Post content violates guidelines")
        # Admin users have the ability to verify content
        super().create_post(content)

    def verify_content(self, content):
        # Some content verification logic
        return "spam" not in content

def publish_post(user: User, content: str):
    try:
        user.create_post(content)
    except ValueError as e:
        print(f"Error: {e}")

def main():
    standard_user = StandardUser()
    admin_user = AdminUser()

    publish_post(standard_user, "Hello World!")  # Works fine
    publish_post(admin_user, "This is a spam post")  # Raises ValueError


if __name__ == "__main__":
    main()
    