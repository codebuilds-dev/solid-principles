# SRP Violation: PostManager handling creation and logging

class PostManager:
    def create_and_log_post(self, content):
        print(f"Post created: {content}")
        print(f"Logged post creation: {content}")


def main():
    post_manager = PostManager()
    post_manager.create_and_log_post("This is a combined operation")


if __name__ == "__main__":
    main()
