# SOLID
# Single Responsibility Principle
class SendEmail:
    def send(self, message):
        print(message)


class SendSMS:
    def send(self, message):
        print(message)


# Open/Close Principle
class Notification:
    def send(self, message):
        ...


class NotificationEmail:
    def send(self, message):
        ...


class NotificationSMS:
    def send(self, message):
        ...


# Liskov Substitution Principle
def notification(noti: Notification, message):
    noti.send(message)


# Interface Segregation Principle
# before
class Noti:
    def send_sms(self, message):
        ...

    def send_email(self, message):
        ...


class NotiSMS:
    def send_sms(self, message):
        ...


class NotiEmail:
    def send_email(self, message):
        ...


# Dependency Inversion Principle
# before
class B:
    def __init__(self):
        ...


class A:
    def __init__(self):
        self.b = B()


# after
class A:
    def __init__(self, b):
        self.b = b
