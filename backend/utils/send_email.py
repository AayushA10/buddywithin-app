import smtplib
import ssl
from email.message import EmailMessage
import os

def send_summary_email(to_email: str, subject: str, body: str) -> str:
    sender_email = os.getenv("SENDER_EMAIL")
    sender_pass = os.getenv("SENDER_APP_PASSWORD")  # Use App Password (Gmail)

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email
    msg.set_content(body)

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, sender_pass)
            server.send_message(msg)
        return "✅ Email sent successfully!"
    except Exception as e:
        return f"❌ Failed to send email: {e}"
