import argparse
import json
import sys
from json import JSONDecodeError
from xml.dom import minidom

from module import concat_with, xmltree_create


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


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument(students='students.json',rooms='rooms.json',format_='')
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
