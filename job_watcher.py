import os
import requests
import smtplib
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)

SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = os.getenv('SMTP_PORT')
EMAIL_FROM = os.getenv('EMAIL_FROM')  # sending email
EMAIL_TO = os.getenv('EMAIL_TO') # receiving email
EMAIL_USERNAME = os.getenv('EMAIL_USERNAME')  # Brevo login 
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')  # Your master SMTP password

# Job listings page
JOB_URL = "https://jobs.lever.co/hallow"
KEYWORDS = ["developer", "engineer"]


# Debug for SMTP Email settings

# def send_test_email(content):
#     try:
#         msg = MIMEText(content)
#         msg['Subject'] = "Daily Hallow Job Watcher Update"
#         msg['From'] = EMAIL_FROM
#         msg['To'] = EMAIL_TO

#         server = smtplib.SMTP(SMTP_SERVER, int(SMTP_PORT))
#         server.starttls()
#         server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
#         server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
#         server.quit()
#         print("Email sent successfully!")
#     except Exception as e:
#         print("Failed to send email:", e)

# send_test_email("Test email from Brevo SMTP service.")


def fetch_job_listings():
    """Fetch job listings from the Hallow job board and return formatted results."""
    response = requests.get(JOB_URL)
    if response.status_code != 200:
        return "Failed to retrieve job listings."

    soup = BeautifulSoup(response.text, 'html.parser')
    job_titles = soup.find_all('h5')
    job_list = []

    for job in job_titles:
        job_text = job.get_text(strip=True)
        
        # Check for keyword matches
        highlighted = any(keyword in job_text.lower() for keyword in KEYWORDS)
        
        if highlighted:
            # Highlight matches with bold and yellow background
            formatted_text = f'<li><b><span style="background-color: yellow;">{job_text}</span></b></li>'
        else:
            formatted_text = f'<li>{job_text}</li>'
        
        job_list.append(formatted_text)

    if not job_list:
        return "No job postings found."

    # Create email body with job listings and a link to the site
    email_body = (
        "<p>Here are the latest job postings from Hallow:</p>"
        "<ul>" + "".join(job_list) + "</ul>"
        f'<p><a href="{JOB_URL}">Click here to view all job postings.</a></p>'
    )

    return email_body

def send_email():
    """Send the job listings email."""
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

# Run the function to send the email
send_email()