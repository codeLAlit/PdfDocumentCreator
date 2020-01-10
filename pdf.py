from reportlab.pdfgen import canvas
import json
import functions as f
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0
from reportlab.pdfbase import pdfmetrics
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import sys

with open('data2.json') as data_file:
    data = json.load(data_file)
# data_str=sys.argv[1]
# # data = json.load( sys.stdin )
# print(data_str)
# data=json.loads(data_str)
param=[]

param=f.makeParam(data)

horz_k=100
horz_val=0
indent=10
lineSpacing=30

def sendMail(recAdd):
    fromaddr = "jltiitb2019@gmail.com"
    toaddr = recAdd

    msg = MIMEMultipart()    
    msg['From'] = fromaddr  
    msg['To'] = toaddr  
    msg['Subject'] = "Response Form"
    body = "Here is the pdf of your response:"
    msg.attach(MIMEText(body, 'plain')) 
    filename = "hello.pdf"
    attachment = open("hello.pdf", "rb")
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

def writeTextTo(c):
    ver=700
    for item in param:
        if str(type(data[item])).find('dict')!=-1:
            c.setFont('Times-Bold', 16)
            c.drawString(horz_k, ver, item.capitalize()+":")
            ver=ver-lineSpacing
            if ver < 50:
                c.showPage()
                ver=750

            horz_d=horz_k+c.stringWidth(item, 'Times-Roman', 16)+indent
            for subItems in data[item]:
                c.setFont('Times-Bold', 16)
                c.drawString(horz_d, ver, subItems.capitalize()+":")
                c.setFont('Courier', 16)
                horz_val=horz_d+c.stringWidth(subItems, 'Times-Roman', 16)+indent
                c.drawString(horz_val, ver, str(data[item][subItems]))
                ver=ver-lineSpacing
                if ver < 50:
                    c.showPage()
                    ver=750


        elif str(type(data[item])).find('list')!=-1:
            c.setFont('Times-Bold', 16)
            c.drawString(horz_k, ver, item.capitalize()+":")
            horz_val=horz_k+c.stringWidth(item, 'Times-Roman', 16)+indent
            for subItems in data[item]:
                c.setFont('Courier', 16)                
                c.drawString(horz_val, ver, str(subItems))
                ver=ver-lineSpacing
                if ver < 50:
                    c.showPage()
                    ver=750

        else:
            c.setFont('Times-Bold', 16)
            c.drawString(horz_k, ver, item.capitalize()+":")
            horz_val=horz_k+c.stringWidth(item, 'Times-Roman', 16)+indent
            c.setFont('Courier', 16)
            c.drawString(horz_val, ver, str(data[item]))
            ver=ver-lineSpacing
            if ver < 50:
                c.showPage()
                ver=750
        

c=canvas.Canvas("hello.pdf")
writeTextTo(c)
c.showPage()
c.save()
sendMail(data["Email ID"])

 

