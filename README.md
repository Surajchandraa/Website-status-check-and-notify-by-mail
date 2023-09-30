# Website-status-check-and-notify-by-mail

## Use of this softwere:
- "It checks the status of the website, whether it has crashed or not. If the status changes from crashed to accessible, or vice versa, it notifies through Gmail."This Python script monitors the status of a website and sends email notifications when the website goes down or becomes accessible again.

## How It Works:
- The script uses the requests library to send HTTP requests to the specified website. 
- If the response status code is 200, the website is considered up. If an exception occurs (indicating a connection error), the website is considered down.
- The script keeps track of the website's status using a file named webcrash.txt. If the status changes (from up to down or vice versa), it sends an email notification using the provided Gmail credentials.

## Setup:
- Install the required libraries by running pip install requests.
- Provide your Gmail credentials in the server.login() function. Note: For security reasons, it's recommended to use an App Password for your Gmail account.
- Replace the placeholders in server.sendmail() with your Gmail address as the from_addr and the recipient's Gmail address as to_addrs.
- Set the website_url variable to the URL of the website you want to monitor.

## Note:
- Ensure that you have allowed less secure apps to access your Gmail account, or use an App Password for authentication.
- This script assumes that you have the required SMTP server settings for Gmail. If you're using a different email provider, you may need to adjust the SMTP server and port.


## Best usage:
- Run the script, and it will periodically check the status of the website. If a change in status is detected, it will send an email notification.
- [Use it with amazon web server or other webserver, Set a cronjob and this code will run after each 10 minutes or according to time you set. And if status of website changes anytimes in the day it will notify you using gmail.]

## Output from aws:
<img src="https://github.com/Surajchandraa/Website-status-check-and-notify-by-mail/blob/main/screenshots_of_output/1694707998134.jpg" width="400" height="600">


