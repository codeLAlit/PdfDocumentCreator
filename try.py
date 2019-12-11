import json

with open('data.json') as data_file:
    data = json.load(data_file)

dat = str(data)
print(type(data["name"]))


if str(type(data["name"])).find('list')!=-1:
    print(1)
else:
    print(0)


c.drawString(horz_k, ver, item.capitalize())
        horz_val=horz_k+len(item)+indent
        c.drawString(horz_val, ver, str(data[item]))
        ver=ver-lineSpacing