from abc import ABC, abstractmethod
#abastact product
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass
#concrete products
class Email(Notification):
    def send(self):
        print("Email Notification Sent")
class SMS(Notification):
    def send(self):
        print("SMS Notifcation Sent")
class Push(Notification):
    def send(self):
        print("Push Notification Sent")
#abstract factory creator
class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self):
        pass
class EmailFactory(NotificationFactory):
    def create_notification(self):
        return Email()
class SMSFactory(NotificationFactory):
    def create_notification(self):
        return SMS()
class PushFactory(NotificationFactory):
    def create_notification(self):
        return Push()
#Client
factory = PushFactory()
notification = factory.create_notification()
notification.send()
