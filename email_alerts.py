import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

def send_email_alert(endpoint, error, email_config, sender_email, sender_password):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email_config['receiver']
    msg['Subject'] = f"ALERT: API Failure Detected"

    body = f"""
An issue was detected with the following API endpoint:

Endpoint: {endpoint}
Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}
Error Type: {error}

Recommended Action:
- Investigate the endpoint response
- Check upstream services or network issues
- Contact support team if unresolved

This is an automated alert from your API Monitor.
"""

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(email_config['smtp_server'], email_config['port'])
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email_config['receiver'], msg.as_string())
        server.quit()
        print(f"[✔] Alert email sent for {endpoint}")
    except Exception as e:
        print(f"[X] Failed to send email: {str(e)}")
