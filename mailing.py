import smtplib
from os import environ


def send_email(email: str, message: str, contact_email: str) -> None:
    with smtplib.SMTP(host="smtp-mail.outlook.com", port=587) as connection:
        connection.starttls()
        connection.login(user=environ['EMAIL'], password=environ['PASSWORD'])
        connection.sendmail(
            from_addr=environ['EMAIL'],
            to_addrs=email,
            msg=f"Subject:{contact_email} want to contact you!\n\n{message}"
        )
