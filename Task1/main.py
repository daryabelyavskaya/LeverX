import sys
import json
from json import JSONEncoder
import xml.etree.ElementTree as ET



class Room(JSONEncoder):

    def __init__(self, id: int, name: str, students_list: list):
        self.id = id
        self.name = name
        self.students_list = students_list


def main():
    students = "students.json"
    rooms = "rooms.json"
    output = 'xml'
    # students, rooms, output = args[1:]
    data_students = json.loads(open(students, 'r', encoding='utf-8').read())
    data_rooms = json.loads(open(rooms, 'r', encoding='utf-8').read())
    dict = {}
    for student in data_students:
        if dict.get(student['room']) is None:
            dict[student['room']] = [student]
        else:
            dict[student['room']].append(student)
    result = []
    for room in data_rooms:
        result.append(Room(room['id'], room['name'], dict[room['id']]))
    with open('result.json','w') as res:
        json.dump(result,res,default=lambda x: x.__dict__)
    root = ET.Element('Rooms')
    for r in result:
        room = ET.SubElement(root,r.name)
        ET.SubElement(room, 'id').text = str(r.id)
        ET.SubElement(room, 'Students')
    tree = ET.ElementTree(root)
    with open('result.xml', 'w') as res2:
        tree.write('result.xml')






main()

# main(sys.argv)
