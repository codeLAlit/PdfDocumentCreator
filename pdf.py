from reportlab.pdfgen import canvas
import json
import functions as f

with open('data.json') as data_file:
    data = json.load(data_file)

param=[]

param=f.makeParam(data)

horz_k=100
horz_val=0
indent=50
lineSpacing=20

def writeTextTo(c):
    ver=700
    for item in param:
        if str(type(data[item])).find('dict')!=-1:
            c.drawString(horz_k, ver, item.capitalize()+":")
            ver=ver-lineSpacing
            horz_d=horz_k+len(item)+indent
            for subItems in data[item]:
                c.drawString(horz_d, ver, subItems.capitalize()+":")
                horz_val=horz_d+len(subItems)+indent
                c.drawString(horz_val, ver, str(data[item][subItems]))
                ver=ver-lineSpacing

        elif str(type(data[item])).find('list')!=-1:
            c.drawString(horz_k, ver, item.capitalize()+":")
            horz_val=horz_k+len(item)+indent
            for subItems in data[item]:                
                c.drawString(horz_val, ver, str(subItems))
                ver=ver-lineSpacing

        else:
            c.drawString(horz_k, ver, item.capitalize()+":")
            horz_val=horz_k+len(item)+indent
            c.drawString(horz_val, ver, str(data[item]))
            ver=ver-lineSpacing
        

c=canvas.Canvas("hello.pdf")
writeTextTo(c)
c.showPage()
c.save()


