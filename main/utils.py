from django.core.mail import EmailMessage,send_mass_mail


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        send_mass_mail(email.send())
        send_mass_mail(email)

