import xml.etree.cElementTree as ET


def concat_with(data_students, data_rooms):
    for student in data_students:
        if data_rooms[student['room']].get('students') is None:
            data_rooms[student['room']]['students'] = [student]
        else:
            data_rooms[student['room']]['students'].append(student)
    return data_rooms


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
