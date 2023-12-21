# ISP: Interfaces for user actions

from abc import abstractmethod

class Postable:
    @abstractmethod
    def post(self, content):
        pass


class Commentable:
    @abstractmethod
    def comment(self, post_id, text):
        pass


class Likable:
    @abstractmethod
    def like(self, post_id, liked):
        pass


class SocialMediaUser(Postable, Commentable):
    def post(self, content):
        print(f"Posting content: {content}")

    def comment(self, post_id, text):
        print(f"Commenting on post {post_id}: {text}")


def main():
    user = SocialMediaUser()
    user.post("Sharing a new post!")
    user.comment(101, "This is a great post!")


if __name__ == "__main__":
    main()
