import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import uuid
from SRC.db import mark_email_sent, add_email_log

load_dotenv()

GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

def send_email(user_email, recipient, subject, body, scheduled_time):
    """
    Send email via Gmail and track sending/opening
    """
    track_code = str(uuid.uuid4())
    tracking_pixel = f"<img src='http://127.0.0.1:8000/track/{track_code}' width='1' height='1' />"
    body_html = body + tracking_pixel

    msg = MIMEMultipart("alternative")
    msg["From"] = GMAIL_USER
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(body_html, "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
            server.sendmail(GMAIL_USER, recipient, msg.as_string())

        mark_email_sent(user_email, subject, recipient, scheduled_time)
        add_email_log(user_email, recipient, subject, "sent", "Email sent successfully")
        return track_code
    except Exception as e:
        add_email_log(user_email, recipient, subject, "failed", str(e))
        return None
