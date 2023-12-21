# OCP Violation: Analytics class

class Analytics:
    def analyze(self, post, post_type):
        if post_type == "text":
            print(f"Analyzing text post: {post}")
        elif post_type == "image":
            print(f"Analyzing image post: {post}")


def main():
    analytics = Analytics()
    analytics.analyze("Text post content", "text")
    analytics.analyze("Image post content", "image")


if __name__ == "__main__":
    main()
