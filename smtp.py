import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()

mesaj["From"] = "kucukbolukbasali@gmail.com"

mesaj["To"] = "aydinahmetkadir@gmail.com"

mesaj["Subject"] = "SMTP ile mail gönderme"

yazi = """

Python'daki SMTP modülü ile mail gönderiyorum.

Fazla dikkate alma deneme için yaptım.

ALİ KÜÇÜKBÖLÜKBAŞ
"""

mesaj_govdesi =MIMEText(yazi,"plain")

mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)

    mail.ehlo()

    mail.starttls()

    mail.login("kucukbolukbasali@gmail.com","1903kartal1903")

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

    print("Mail Başarı ile gönderildi..")

    mail.close()
except:
    sys.stderr.write("Bir sorun oluştu...")
    sys.stderr.flush()

