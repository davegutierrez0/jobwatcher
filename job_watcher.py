import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Sendinblue SMTP Configuration
SMTP_SERVER = "smtp-relay.brevo.com"
SMTP_PORT = 587
EMAIL_FROM = os.getenv('EMAIL_FROM')  # Your Brevo-registered email
EMAIL_TO = os.getenv('EMAIL_TO')      # Your Gmail address
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')  # Your Sendinblue SMTP key

def send_email(content):
    try:
        msg = MIMEText(content)
        msg['Subject'] = "Daily Hallow Job Watcher Update"
        msg['From'] = EMAIL_FROM
        msg['To'] = EMAIL_TO

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email:", e)

# Example usage
send_email("Test email from Brevo SMTP service.")