#https://www.hackerrank.com/challenges/xml-1-find-the-score/problem?isFullScreen=true

import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    # your code goes here
    cnt = 0
    if node is not None:
        cnt += len(node.attrib)
        for child in node:
            cnt += get_attr_number(child)
    return cnt


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
