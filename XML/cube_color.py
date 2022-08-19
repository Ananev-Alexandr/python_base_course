import xml.etree.ElementTree as ET


color = {'red': 0, 'green': 0, 'blue': 0}


def getchildren(element, lvl=1):
    if element.findall('cube'):
        for i in element.findall('cube'):
            getchildren(i, lvl+1)
    color[element.attrib['color']] += lvl


tree = ET.ElementTree(ET.fromstring(input()))
root = tree.getroot()
getchildren(root)
print(color['red'], color['green'], color['blue'])
