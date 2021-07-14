import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html=Template(Path('index.html').read_text())
email=EmailMessage()
email['from']='Geeksfromindia'
email['to']='receiveremail.com'
email['subject']='This is Py email'

email.set_content(html.substitute({'name':'Jathi ratnam'}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('email id','password')
  smtp.send_message(email)
  print('done!')