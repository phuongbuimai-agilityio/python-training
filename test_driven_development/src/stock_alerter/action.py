import smtplib
from email.mime.text import MIMEText


class PrintAction:
    def execute(self, content):
        print(content)


class EmailAction:
    """Send an email when a rule is matched"""

    from_email = "alerts@stocks.com"

    def __init__(self, to: str) -> None:
        self.to_email = to

    def execute(self, content: str) -> None:
        """Send an email using SMTP.

        Args:
            content (str): The content of the email.
        """
        msg = MIMEText(content)
        msg["Subject"] = "New Stocks Alert"
        msg["From"] = self.from_email
        msg["To"] = self.to_email

        smtp = smtplib.SMTP("email.stocks.com")
        try:
            smtp.send_message(msg)
        finally:
            smtp.quit()
