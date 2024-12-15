# Access Exel documents
import os
from openpyxl import Workbook, load_workbook
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd


# To sleep a few second between emails
import time

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage
# set up the SMTP server


filename = "..."
sheetname = "..."


def ask_for_password() -> str:
    print(username + ", ", end="")
    return input("enter your password: ")


def login_smtp(username: str, password: str) -> smtplib.SMTP:
    s = smtplib.SMTP(host='mail.bfh.ch', port=587)
    s.starttls()
    s.login(username, password)
    return s


def send_mail(smtp: smtplib.SMTP, receive_email: str, subject: str, html_content: str):
    sender_email = "zahnk2@bfh.ch"

    msg = MIMEMultipart("mixed")
    msg["From"] = sender_email
    msg["To"] = receive_email
    msg["Subject"] = subject
    # msg.set_content(content)

    alternative_part = MIMEMultipart("alternative")

    # Add HTML content
    html_part = MIMEText(html_content, "html")
    alternative_part.attach(html_part)

    # Attach the alternative part to the main message
    msg.attach(alternative_part)

    try:
        smtp.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        smtp.quit()


def read_excel_get_html(path: str) -> str:
    try:
        df = pd.read_excel(path)
        html = df.to_html(index=False, escape=False, border=1)
        return html
    except Exception as e:
        print(e)
        exit(0)


if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    excel_path = os.path.join(current_directory, "../rsc/marking-sample.xlsx")
    html = read_excel_get_html(excel_path)

    username = "zahnk2"
    password = ask_for_password()
    smtp = login_smtp(username, password)

    send_mail(smtp, "kevin.zahn@bluewin.ch", "Python", html)
