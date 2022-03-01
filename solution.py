def num1():
    import psutil
    from pprint import pprint
    print("Информация о устройстве:")
    pprint(psutil.disk_partitions())


def num2():
    import os

    i = input()
    f = open("files.txt", "w")
    f.write(i)
    f.close()
    with open("files.txt", "r") as f:
        mes = f.read()
    print(mes)
    os.remove("files.txt")


def num3():
    import os
    import json

    data = input()
    to_json = {'message': data}
    with open('file.json', 'w') as fj:
        fj.write(json.dumps(to_json))

    with open('file.json') as fj:
        print(fj.read())

    os.remove('file.json')


def num4():

    import xml.etree.ElementTree as ElT
    import os

    print("Input on Eng")
    first_name = input("First Name: ")
    second_name = input("Second Name: ")
    city = input("City: ")
    items = [
        {"first_name": first_name, "second_name": second_name, "city": city},
    ]
    root = ElT.Element('root')
    for i, item in enumerate(items, 1):
        person = ElT.SubElement(root, 'person' + str(i))
        ElT.SubElement(person, 'first_name').text = item['first_name']
        ElT.SubElement(person, 'second_name').text = item['second_name']
        ElT.SubElement(person, 'city').text = item['city']

    tree = ElT.ElementTree(root)
    tree.write('xmlf.xml')

    with open('xmlf.xml') as f:
        print(f.read())

    os.remove('xmlf.xml')


def num5():

    import os
    import zipfile

    i = input()
    newzip = zipfile.ZipFile('ossol.zip', 'w')
    fz = open("file.txt", "w")
    fz.write(i)
    fz.close()
    newzip.write('file.txt')
    os.remove("file.txt")
    while True:
        x = int(input("Показать содержимое файла: 1->да / 2->извлечь файл / 3->удалить"))
        if x == 0:
            break
        elif x == 1:
            newzip.printdir()
        elif x == 2:
            newzip.extract('file.txt')
            with open("file.txt", "r") as fz:
                y = fz.read()
                print(y)
                fz.close()
        elif x == 3:
            newzip.close()
            os.remove("ossol.zip")
            try:
                os.remove("file.txt")
            except FileNotFoundError:
                pass
            else:
                os.remove("file.txt")
            break



