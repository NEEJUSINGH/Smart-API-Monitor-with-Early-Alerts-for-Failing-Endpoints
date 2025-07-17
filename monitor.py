import requests
import time
import csv
import json
from email_alerts import send_email_alert
from secrets import EMAIL_ADDRESS, EMAIL_PASSWORD

# Load config
with open('config.json') as f:
    config = json.load(f)

endpoints = config['endpoints']
email_config = config['email']
alert_threshold = config.get('alert_threshold', 3)
check_interval = config.get('check_interval', 60)

failure_counts = {url: 0 for url in endpoints}

def log_failure(endpoint, error_type):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    with open('error_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, endpoint, error_type])

def check_api(endpoint):
    try:
        response = requests.get(endpoint, timeout=5)
        if response.status_code >= 400:
            return f"Status code {response.status_code}"
        try:
            response.json()
        except Exception:
            return "Malformed JSON"
        return None  # No issues
    except requests.exceptions.Timeout:
        return "Timeout"
    except Exception as e:
        return str(e)

while True:
    print("\nChecking APIs...")
    for url in endpoints:
        error = check_api(url)
        if error:
            failure_counts[url] += 1
            log_failure(url, error)
            print(f"[!] {url} failed: {error}")
            if failure_counts[url] >= alert_threshold:
                send_email_alert(url, error, email_config, EMAIL_ADDRESS, EMAIL_PASSWORD)
                failure_counts[url] = 0  # reset after alert
        else:
            failure_counts[url] = 0  # reset on success
            print(f"[✓] {url} OK")
    time.sleep(check_interval)
