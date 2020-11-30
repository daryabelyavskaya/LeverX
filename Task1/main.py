import json
import sys
import xml.etree.cElementTree as ET
from json import JSONDecodeError
from xml.dom import minidom

from module import concat_with, xmltree_create, arguments_parse


class Parser:
    def serialized_to(self):
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


def main(args: list):
    args = arguments_parse(args)
    students, rooms, format_ = args.students, args.room, args.format
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
