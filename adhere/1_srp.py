# SRP: PostCreator and PostLogger

class PostCreator:
    def create_post(self, content):
        # Logic to add a new post
        print(f"Post created: {content}")
        return content


class PostLogger:
    def log_post(self, action, post):
        # Logic to log an action on a post
        print(f"Action: {action} on post: {post}")


def main():
    post_creator = PostCreator()
    new_post = post_creator.create_post("Hello, this is my first post!")

    post_logger = PostLogger()
    post_logger.log_post("Created", new_post)


if __name__ == "__main__":
    main()
