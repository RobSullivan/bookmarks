# -*- coding: utf-8 -*-

"""
An alternative regex free way of getting the links

"""

from lxml import etree


bookmarks = open('bookmarks.html')
parser = etree.HTMLParser()
tree = etree.parse(bookmarks, parser)

root = tree.getroot()

links = (a.attrib['href'] for a in root.iterdescendants('a'))

