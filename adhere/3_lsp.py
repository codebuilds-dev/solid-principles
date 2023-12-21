# LSP: User and its subclasses

class User:
    def create_post(self, content):
        # Common post creation logic
        print(f"Creating post: {content}")
        return True


class StandardUser(User):
    def create_post(self, content):
        # Standard users can create posts normally
        return super().create_post(content)


class AdminUser(User):
    def create_post(self, content):
        if self.verify_content(content):
            # Admin users have the ability to verify content
            return super().create_post(content)

        print("Post content did not pass verification.")
        return False

    def verify_content(self, content):
        # Some content verification logic
        return "spam" not in content


def publish_post(user: User, content: str):
    success = user.create_post(content)
    if success:
        print("Post published successfully.")
    else:
        print("Post publication failed.")


def main():
    standard_user = StandardUser()
    admin_user = AdminUser()

    # Output: Post published successfully.
    publish_post(standard_user, "Hello World!")
    # Output: Post content did not pass verification. Post publication failed.
    publish_post(admin_user, "This is a spam post")


if __name__ == "__main__":
    main()






















# class Shape:
#     def calculate_area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def calculate_area(self):
#         return self.width * self.height

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def calculate_area(self):
#         return self.side * self.side

# def print_area(shape: Shape):
#     print(f"The area is: {shape.calculate_area()}")

# def main():
#     rectangle = Rectangle(5, 4)
#     square = Square(5)

#     print_area(rectangle)  # Outputs: The area is: 20
#     print_area(square)    # Outputs: The area is: 25


# if __name__ == "__main__":
#     main()
