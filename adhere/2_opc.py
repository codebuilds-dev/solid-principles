# OCP: Analytics classes

from abc import ABC, abstractmethod

class PostAnalytics(ABC):
    @abstractmethod
    def analyze(self, post):
        pass


class TextPostAnalytics(PostAnalytics):
    def analyze(self, post):
        # Specific analytics for text posts
        print(f"Analyzing text post: {post}")


class ImagePostAnalytics(PostAnalytics):
    def analyze(self, post):
        # Specific analytics for image posts
        print(f"Analyzing image post: {post}")

class VideoPostAnalytics(PostAnalytics):
    def analyze(self, post):
        # Specific analytics for video posts
        print(f"Analyzing video post: {post}")


def main():
    text_post_analytics = TextPostAnalytics()
    text_post_analytics.analyze("Text post content")

    image_post_analytics = ImagePostAnalytics()
    image_post_analytics.analyze("Image post content")


if __name__ == "__main__":
    main()
