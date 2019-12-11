from reportlab.pdfgen import canvas
import json
import functions as f
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0
from reportlab.pdfbase import pdfmetrics

with open('data.json') as data_file:
    data = json.load(data_file)

param=[]

param=f.makeParam(data)

horz_k=100
horz_val=0
indent=10
lineSpacing=30

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


