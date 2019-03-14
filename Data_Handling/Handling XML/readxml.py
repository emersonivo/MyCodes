from xml.etree import ElementTree as ET
tree = ET.parse("sample.xml")
root = tree.getroot()
import datetime
from datetime import date, timedelta

def GOOD_TO_UPDATE():
    for user in root:
        if "012345" in user.get("id"):
            for attr in user:
                if "attrib1" in attr.get("name"):
                    for event in attr:
                        if "last_seem" in event.tag:
                            event.set('status', 'GRANTED')

    tree.write('sample2.xml')

def GOOD_APPEND_OR_UPDATE():
    User = "012345"
    Attrib = "attrib3"
    EXIST = False
    Status = "REQUESTED"
    DATE = date.today()
    for user in root:
        if User in user.get("id"):
            if not user.find('.//res/[@name=\"'+Attrib+'\"]') and not EXIST:
                newattr = ET.SubElement(user, 'res', attrib={'name:'Attrib})
                first_seem = ET.SubElement(newattr, 'first_seem', attrib={'date':DATE.strftime('%Y-%m%d'), 'status':Status})
                last_seem = ET.SubElement(newattr, 'last_seem', attrib={'date':DATE.strftime('%Y-%m-%d'), 'status':Status})
                ET.dump(newattr)
                EXIST = True
            elif user.find('.//res/[@name=\"'+Attrib+'\"]'):
                for attr in user:
                    if Attrib in attr.get("name"):
                        for event in attr:
                            if "last_seem" in event.get("name"):
                                event.set('date', DATE.strftime('%Y-%m%d'))
                                event.set('status', Status)

    tree.write('sample.xml')

def GOOD_GET_DATES_DIFF():
    User = "012345"
    Attrib = "attrib3"
    Status = "REQUESTED"
    for user in root:
        if User in user.get("id"):
            if user.find('.//res/[@name=\"'+Attrib+'\"]'):
                for attr in user:
                    if Attrib in attr.get("name"):
                        for event in attr:
                            if "first_seem" in event.get("name"):
                                first_seem = datetime.datetime.strptime(event.get("date"), '%Y-%m-%d')
                            if "last_seem" in event.get("name"):
                                last_seem = datetime.datetime.strptime(event.get("date"), '%Y-%m-%d')

    diffdates = last_seem - first_seem
    if first_seem < (last_seem - timedelta(1)):
        print "OUTDATE Event"
