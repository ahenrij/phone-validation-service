"""Twilio utilities."""

import logging
from typing import Optional
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from src.core.config import settings


logger = logging.getLogger(__name__)
client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)


def send(to: str, body: str) -> Optional[dict]:
    """Send SMS message.

    Following the Twilio API doc: https://www.twilio.com/docs/sms/tutorials/how-to-send-sms-messages-python
    """
    try:
        message = client.messages.create(from_=settings.TWILIO_SENDER, to=to, body=body)
        return message
    except TwilioRestException as e:
        logger.error(e.msg)
        return None
