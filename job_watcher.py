import os
import requests
import smtplib
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(override=True)

# SMTP email settings
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = os.getenv('SMTP_PORT')
EMAIL_FROM = os.getenv('EMAIL_FROM')  # Sender email address
EMAIL_TO = os.getenv('EMAIL_TO')  # Receiver email address
EMAIL_USERNAME = os.getenv('EMAIL_USERNAME')  # Brevo SMTP username
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')  # Brevo SMTP password

# Job board URL and search keywords
JOB_URL = os.getenv('JOB_URL', 'https://jobs.lever.co/hallow')
KEYWORDS = os.getenv('KEYWORDS', 'developer,engineer').split(',')
JOB_TITLE_HTML_TAG = 'h5' # Change depending on how the individual posts are formatted

def fetch_job_listings():
    """
    Fetch job listings from the provided job board URL and return formatted results.
    Highlights job titles that contain specified keywords.
    """
    response = requests.get(JOB_URL)
    if response.status_code != 200:
        return "Failed to retrieve job listings."

    soup = BeautifulSoup(response.text, 'html.parser')
    job_titles = soup.find_all()
    job_list = []

    for job in job_titles:
        job_text = job.get_text(strip=True)
        
        # Highlight job titles that match any keyword
        highlighted = any(keyword.lower() in job_text.lower() for keyword in KEYWORDS)
        
        if highlighted:
            formatted_text = f'<li><b><span style="background-color: yellow;">{job_text}</span></b></li>'
        else:
            formatted_text = f'<li>{job_text}</li>'
        
        job_list.append(formatted_text)

    if not job_list:
        return "No job postings found."

    # Prepare email content with job listings and a link to the website
    email_body = (
        "<p>Here are the latest job postings from Hallow:</p>"
        "<ul>" + "".join(job_list) + "</ul>"
        f'<p><a href="{JOB_URL}">Click here to view all job postings.</a></p>'
    )

    return email_body

def send_email():
    """
    Send an email with the job listings.
    The email is sent as HTML content.
    """
    content = fetch_job_listings()

    msg = MIMEText(content, "html")  # Send email as HTML
    msg['Subject'] = "🛠️ Hallow Job Listings - Daily Update"
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO

    try:
        server = smtplib.SMTP(SMTP_SERVER, int(SMTP_PORT))
        server.starttls()
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email:", e)

if __name__ == "__main__":
    send_email()