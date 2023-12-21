# DIP: Notification service and manager

from abc import ABC, abstractmethod


class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass


class EmailNotificationService(NotificationService):
    def send_notification(self, message):
        print(f"Sending email: {message}")

class PushNotificationService(NotificationService):
    def send_notification(self, message):
        print(f"Sending push notification: {message}")


class NotificationManager:
    def __init__(self, service: NotificationService):
        self.service = service

    def notify(self, message):
        self.service.send_notification(message)

# import unittest
# from unittest.mock import Mock

# class TestNotificationManager(unittest.TestCase):

#     def test_notify_calls_send_notification(self):
#         # Create a mock NotificationService
#         mock_service = Mock()

#         # Create a NotificationManager with the mock service
#         manager = NotificationManager(mock_service)

#         # Call the notify method
#         manager.notify("Test Message")

#         # Assert that send_notification was called once with the correct message
#         mock_service.send_notification.assert_called_once_with("Test Message")

# if __name__ == '__main__':
#     unittest.main()

# def main():
#     # email_notification_service = EmailNotificationService()
#     push_notification_service = PushNotificationService()

#     notification_manager = NotificationManager(push_notification_service)
#     notification_manager.notify("You have a new follower!")


# if __name__ == "__main__":
#     main()
