# Smart API Monitor with Early Alerts for Failing Endpoints

This project is a lightweight Python-based monitoring tool designed to detect failing or unstable API endpoints and proactively notify the support team via email. It simulates a real-world need: when a client-facing API fails silently, it can lead to broken workflows, frustrated users, and delayed fixes.

The monitor runs on a configurable schedule, checks multiple endpoints for availability, response time, and error codes (like 4xx/5xx), and sends a clear, human-readable email alert when an issue is detected. It also tracks repeated failures and escalates when necessary.

### Why I Built This

In environments where APIs connect critical systems—ads platforms, CRMs, student portals, or payment systems—failures often go unnoticed until users complain. I wanted to build something that gives support engineers or clients a heads-up before issues become outages. This project allowed me to combine scripting, error handling, communication logic, and automation into one tool that quietly makes things better behind the scenes.

### Key Features

- Monitor any number of REST API endpoints via a config file
- Detects failures like:
  - Timeout
  - Slow response
  - 4xx/5xx status codes
  - Invalid/malformed JSON
- Logs timestamped incidents to `.csv` or `.json`
- Sends formatted email alerts with context and recommendations
- Optional escalation logic if issues persist
- Easy to extend or adapt for real-world teams

### Technologies Used

- Python
- `requests` (HTTP)
- `smtplib` / Gmail SMTP (for email)
- `json`, `time`, `csv`, `logging`
- Optional: `Streamlit` for dashboard (if added)

### How to Use

#### 1. Clone the Repository
```bash
git clone https://github.com/NEEJUSINGH/api-monitor-alerts.git
cd api-monitor-alerts
```
#### 2. Install Dependencies
```bash
Make sure you have Python 3 installed. Then, install required packages:
pip install -r requirements.txt
```
#### 3. Configure Your Endpoints
```bash
Open config.json and add the API endpoints you want to monitor. Example:
{
  "endpoints": [
    "https://example.com/api/health",
    "https://another-api.com/status"
  ],
  "email": {
    "sender": "youremail@example.com",
    "receiver": "alertrecipient@example.com",
    "smtp_server": "smtp.gmail.com",
    "port": 587
  },
  "alert_threshold": 3,
  "check_interval": 60
}
```
#### 4. Set Up Email Access
```bash
If using Gmail, enable “less secure apps” or use an app password (for accounts with 2FA).
Add your credentials in secrets.py like this:
EMAIL_ADDRESS = "youremail@example.com"
EMAIL_PASSWORD = "yourpassword"
Never commit secrets.py file to GitHub. Use .gitignore to protect it.
```
#### 5. Run the Monitor
```bash
python monitor.py
```

Testing
You can simulate failing endpoints using tools like:
#### Simulate a Server Error (500)
Add this URL to your config.json:
https://httpstat.us/500
This returns a 500 Internal Server Error, which will trigger an alert.


#### Simulate a Timeout
Add this:
https://httpbin.org/delay/10
This delays the response by 10 seconds. If your timeout is set to less than that (e.g., 5 sec), it will be flagged.


Check the Email
When triggered, you should receive an alert email with:

The failing endpoint

Timestamp

Type of error (e.g., timeout, status code)

Suggested next steps
