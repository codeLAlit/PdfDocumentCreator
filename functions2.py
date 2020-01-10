import sys
import os
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

def createPdf(inFile, outFile):
	
	
def mailPdf(file, clientEmail):   
	fromaddr = "jltiitb2019@gmail.com"
	toaddr = clientEmail
	   
	msg = MIMEMultipart()   
	msg['From'] = fromaddr  
	msg['To'] = toaddr
	msg['Subject'] = "Insurance Document"
	body = "This is your response"
	msg.attach(MIMEText(body, 'plain')) 
	filename = "Insurance Document"
	attachment = open(file, "rb") 
	p = MIMEBase('application', 'octet-stream')
	p.set_payload((attachment).read()) 
	encoders.encode_base64(p) 
	p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
	msg.attach(p) 
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	s.starttls() 
	s.login(fromaddr, "jltindia-2019") 
	text = msg.as_string() 
	s.sendmail(fromaddr, toaddr, text)
	s.quit() 
