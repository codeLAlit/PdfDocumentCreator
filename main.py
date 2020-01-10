from __future__ import print_function
from mailmerge import MailMerge
from datetime import date
import json

template="templates/master.docx"
database="databases/data.json"

file=MailMerge(template)

with open(database) as data_file:
	data=json.load(data_file)

personalInfo=data["personal_info"]
	
client_name=personalInfo["client_name"]
vehiclesList=data["vehicles"]

createdDoc="docx/"+client_name.replace(" ","")+".docx"

file.merge(**personalInfo)


file.merge_rows('vehicle_no', vehiclesList)
file.merge_rows('summ_vehicle_no', vehiclesList)

file.write(createdDoc)