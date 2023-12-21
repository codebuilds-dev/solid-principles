# ISP Violation: UserActions interface

class UserActions:
    def post(self, content):
        pass

    def comment(self, post_id, text):
        pass

    def like(self, post_id, liked):
        pass


class SocialMediaUser(UserActions):
    def post(self, content):
        print(f"Posting: {content}")

    def comment(self, post_id, text):
        pass

    def like(self, post_id, liked):
        pass



def main():
    user = SocialMediaUser()
    user.post("A new post")
    user.comment(123, "Nice post!")
    user.like(123, True)


if __name__ == "__main__":
    main()
