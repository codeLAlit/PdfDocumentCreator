from reportlab.pdfgen import canvas
import json

with open('data.json') as data_file:
    data = json.load(data_file)

param=[]
for key, value in data.items():
    param.append(key)

horz_k=100
horz_val=0
indent=50
lineSpacing=20

def writeTextTo(c):
    ver=700
    for item in param:
        c.drawString(horz_k, ver, item.capitalize())
        horz_val=horz_k+len(item)+indent
        c.drawString(horz_val, ver, str(data[item]))
        ver=ver-lineSpacing


c=canvas.Canvas("hello.pdf")
writeTextTo(c)
c.showPage()
c.save()


