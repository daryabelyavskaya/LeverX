import sys
import json
import xml.etree.cElementTree as ET
from json import JSONDecodeError
from xml.dom import minidom


def xmltree_create(new_list):
    root = ET.Element('Rooms')
    for item in new_list:
        room = ET.SubElement(root, f"Room{item['id']}")
        ET.SubElement(room, 'id').text = str(item['id'])
        ET.SubElement(room, 'name').text = item['name']
        stud = ET.SubElement(room, 'Students')
        for _ in item['students']:
            ET.SubElement(stud, 'name').text = _['name']
            ET.SubElement(stud, 'room').text = str(_['room'])
            ET.SubElement(stud, 'id').text = str(_['id'])
    return root


def concat_with(data_students, data_rooms):
    for student in data_students:
        if data_rooms[student['room']].get('students') is None:
            data_rooms[student['room']]['students'] = [student]
        else:
            data_rooms[student['room']]['students'].append(student)
    return data_rooms


class Parser:
    def serialized_to(self):
        raise NotImplementedError

    def deserialization(self):
        raise NotImplementedError


class JSONParser(Parser):
    def serialized_to(self, data):
        with open('result.json', 'w') as res:
            json.dump(data, res, indent=4, default=lambda x: x.__dict__)

    def deserialization(self, file: str):
        return json.loads(open(file, 'r', encoding='utf-8').read()) 


class XMLParser(Parser):
    def serialized_to(self, root):
        with open('result.xml', 'w') as res2:
            xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
            res2.write(xmlstr)


def main(args:[]):
    students, rooms, format_ = args[1:]
    json_parser = JSONParser()
    try:
        data_students = json_parser.deserialization(students)
        data_rooms = json_parser.deserialization(rooms)
    except JSONDecodeError:
        print('File is empty')
        return
    new_list = concat_with(data_students, data_rooms)
    if format_.lower() == 'json':
        json_parser.serialized_to(new_list)
    elif format_.lower() == 'xml':
        xml_parser = XMLParser()
        root = xmltree_create(new_list)
        xml_parser.serialized_to(root)


main(sys.argv)
