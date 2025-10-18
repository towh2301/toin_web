import os
from django.core.management.base import BaseCommand
from django.core.mail import EmailMessage, send_mail
from django.conf import settings


class Command(BaseCommand):
    help = "Send a test email using current EMAIL_BACKEND. Uses TEST_EMAIL_TO from env or DEFAULT_FROM_EMAIL."

    def add_arguments(self, parser):
        parser.add_argument("--to", dest="to", help="Recipient email address")
        parser.add_argument(
            "--html", action="store_true", help="Send HTML email instead of plain text"
        )

    def handle(self, *args, **options):
        to_addr = (
            options.get("to")
            or os.getenv("TEST_EMAIL_TO")
            or settings.DEFAULT_FROM_EMAIL
        )
        subject = "TOIN test email"
        text = "This is a test email sent using Django's configured EMAIL_BACKEND."
        html = "<p><strong>This is a test email</strong> sent using Django's configured EMAIL_BACKEND.</p>"

        self.stdout.write(
            self.style.NOTICE(f"EMAIL_BACKEND = {settings.EMAIL_BACKEND}")
        )
        self.stdout.write(
            self.style.NOTICE(f"DEFAULT_FROM_EMAIL = {settings.DEFAULT_FROM_EMAIL}")
        )
        self.stdout.write(self.style.NOTICE(f"Sending to: {to_addr}"))

        if options.get("html"):
            msg = EmailMessage(subject, html, settings.DEFAULT_FROM_EMAIL, [to_addr])
            msg.content_subtype = "html"
            msg.send(fail_silently=False)
        else:
            send_mail(
                subject,
                text,
                settings.DEFAULT_FROM_EMAIL,
                [to_addr],
                fail_silently=False,
            )

        self.stdout.write(self.style.SUCCESS("Test email sent successfully."))
