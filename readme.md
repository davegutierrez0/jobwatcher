# 🐦 Job Watcher - Brevo SMTP Email Alerts 🚀

Welcome to Job Watcher, your trusty digital assistant that helps you stay ahead in the job hunt because... **the early bird gets the worm!** 🪱 Especially when it comes to snagging those coveted remote jobs! 🌍💼

For my personal purposes, I'm keeping an eye on the job board over at **Hallow** (the awesome Catholic prayer app 🙏), but you can easily customize this script to monitor any website you fancy. 🎯

## 🎉 Features

- **⏰ Automated Job Monitoring:** Scrapes job postings from a specified URL daily.
- **🔍 Keyword Matching:** Alerts are triggered when job titles contain specific words (like `developer`, `engineer`).
- **📧 Email Notifications:** Get job matches or a friendly 'no matches today' message.
- **🔐 Secure Configuration:** Uses `.env` file to protect your secrets.
- **🛠️ Customizable & Extendable:** Tweak search criteria, recipients, and frequency with ease.

## 📋 Requirements

To run this gem, you'll need:

- Python 3.x 🐍
- The following Python packages:
  - `beautifulsoup4` 🍜 (for web scraping)
  - `requests` 📡 (for fetching job listings)
  - `python-dotenv` 🔑 (for managing environment variables)

## ⚠️ Important Note About Brevo

Brevo (formerly Sendinblue) **does not work with free email providers** (like Gmail, Yahoo, etc.). It is best used with a personal domain (e.g., `yourname@yourdomain.com`). Make sure your sender email is verified and authenticated in Brevo to avoid authentication errors.

## 🛠️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/job-watcher.git
   cd job-watcher
   ```

2. **Set up a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file:**

   In the project root directory, create a file named `.env` and add the following:

   ```env
   EMAIL_FROM=your-verified-brevo-email@yourdomain.com
   EMAIL_TO=yourgmail@gmail.com
   EMAIL_USERNAME=your-brevo-smtp-username
   EMAIL_PASSWORD=your-brevo-smtp-key
   SMTP_SERVER=smtp-relay.brevo.com
   SMTP_PORT=587
   ```

5. **Run the script:**

   ```bash
   python job_watcher.py
   ```

## ⚙️ Configuration

- Change the `KEYWORDS` list in `job_watcher.py` to hunt for your dream jobs.
- Swap the target job URL in the `URL` variable.
- Tweak the sender and recipient in the `.env` file.

## 🤖 Automation

To run the script daily:

- **On macOS/Linux:**

  Add a cron job by running:

  ```bash
  crontab -e
  ```

  Add the following line to schedule the script to run at 9 AM daily:

  ```bash
  0 9 * * * /usr/bin/python3 /path/to/job_watcher.py
  ```

- **On Windows:**

  Use Task Scheduler to run the script daily.

## 🤝 Contributing

Fork this repo and bring your own flavor of job-hunting magic! ✨ Some ideas:

- Adding support for multiple job sites 🌐
- Enhancing keyword matching with regex 🧐
- Making email notifications fancier with HTML templates 🖋️

## 📜 License

This project is licensed under the MIT License. Free to use and modify! 🕊️

## 📧 Contact

Got questions? Suggestions? Or just want to chat about the job hunt? Open an issue in the repo or drop me a line. 💌

---

🚀 Give it a whirl and start getting those job alerts today! Happy job hunting! 🏹

