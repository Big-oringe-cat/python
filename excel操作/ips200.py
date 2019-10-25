# -*- coding: utf-8 -*-
#! /usr/bin/python
import xml.etree.ElementTree as ET
import os
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from openpyxl import Workbook

tree = ET.parse("ips200.xml")
root = tree.getroot()

ips_dir={}
priority_dir = {2:"轻微",3:"一般",4:"重要",5:"紧急"}
for i in root[-1].findall("trigger"):

    name = ""
    list = []
    for j in i.findall("name"):
        name = str(j.text).split(" ",-1)[-1]
        list.append(name)
    list.append("")
    list.append("文本")
    list.append("")
    list.append("Y")
    for j in i.findall("priority"):
        list.append(priority_dir[int(j.text)])
    list.append("SNMP")
    for j in i.findall("name"):
        list.append(str(j.text))
    for j in i.findall("url"):
        list.append(str(j.text))
    for j in i.findall("description"):
        list.append(str(j.text))
    for j in i.findall("expression"):
        e=str(j.text)
        for k in re.split(r"\(|\)",e):
            if "type" in k:
                e=k
        list.append(e)
        id1=e.split('value=STRING: ')[-1].strip('\"').split("-")[0]
        id2=e.split('value=STRING: ')[-1].strip('\"').split("-")[-1]
        list.append(int(id1))
        list.append(int(id2))
        
    ips_dir[name]=list

    
wb = Workbook()
sheet = wb.active
for i in ips_dir:
    sheet.append(ips_dir[i])

wb.save(r'ips200.xlsx')

    
    
