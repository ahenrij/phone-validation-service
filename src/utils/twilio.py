"""Twilio utilities."""

from twilio.rest import Client
from src.core.config import settings

client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)


def send(to: str, body: str) -> dict:
    """Send SMS message.

    Following the Twilio API doc: https://www.twilio.com/docs/sms/tutorials/how-to-send-sms-messages-python
    """
    message = client.messages.create(from_=settings.TWILIO_SENDER, to=to, body=body)
    return message
