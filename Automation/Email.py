from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import ssl

# Create Object for MIMEMultipart
kk=MIMEMultipart()

kk['From']='reshma.s@agaramtech.com'
kk['To']='reshma.s@agaramtech.com'
kk['CC']='reshma.s@agaramtech.com'
kk['Subject']='Test Mail'

content="""
This is automatic mail from SMTP
"""

# Define the format of the Text
kk.attach(MIMEText(content,'plain'))

# File Attachment
filepath='D:\\Resh JPDC\\Selenium_Python\\K_Notes\\re.txt'

# Binary conversion rb readbinary
fileinbinary=open(filepath,"rb")

# Application means to file. octate-stream is used for file without extension.
# payload sending file in any format lyk using FTP IP...
payload=MIMEBase("application","octate-stream")
payload.set_payload(fileinbinary.read())

# Fox Excel Sheet, encoding should be used.
encoders.encode_base64(payload)
kk.attach(payload)

# SMTP is a gmail server which ll perform the Actions done here. 587 is a port.
server=smtplib.SMTP("smtp.gmail.com",587)

# starttls-Transfer Layer Security.To convert the content of mail in encrypt format.content or context anything can be used
server.starttls(context=ssl.create_default_context())
server.login("reshma.s@agaramtech.com","InshaAllah@123")

# (to,bcc) but it won't display in to
server.sendmail("reshma.s@agaramtech.com","reshma.s@agaramtech.com",str(kk))
server.close()
