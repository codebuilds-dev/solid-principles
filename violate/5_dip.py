# DIP Violation: NotificationManager directly depending on EmailNotificationService

class EmailNotificationService:
    def send_email(self, message):
        print(f"Sending email: {message}")


class PushNotificationService:
    def send_push(self, message):
        print(f"Sending push notification: {message}")


class NotificationManager:
    def __init__(self):
        self.email_service = EmailNotificationService()

    def notify(self, message):
        self.email_service.send_email(message)


def main():
    notification_manager = NotificationManager()
    notification_manager.notify("You have a new message!")


if __name__ == "__main__":
    main()
