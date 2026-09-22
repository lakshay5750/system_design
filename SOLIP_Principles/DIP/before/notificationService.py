from emailService import EmailService
from smsService import SmsService
class NotificaionService:
    def __init__(self,email_service:EmailService, sms_service:SmsService):
        self.email_service=email_service
        self.sms_service=sms_service
    
    def sendEmail(self,message):
        self.email_service.send_email(message)
    def sendSMS(self,message):
        self.sms_service.send_sms(message)
    
email_service=EmailService()
sms_service=SmsService()
notification=NotificaionService(email_service,sms_service)
notification.sendEmail("HEY good morning")
notification.sendSMS("I am good")

    