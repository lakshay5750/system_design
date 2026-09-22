from EmailService import EmailService
from SmsService import SmsService
from notificationService import NotificationService

email_service=EmailService()
sms_service=SmsService()
service=NotificationService(email_service)
service.notify("HI message is send to the email")