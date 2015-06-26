# -*- coding: utf-8 -*-

"""
An alternative regex free way of getting the links

"""

from lxml import etree



def linksects():
	with open('bookmarks.html') as f:
		parser = etree.HTMLParser()
		tree = etree.parse(f, parser)
		root = tree.getroot()

	# making it a list instead of generator becauase going to pass
	# the whole thing to a spider, yep the whole list...to see 
	# what happens
		links = [a.attrib['href'] for a in root.iterdescendants('a')]

	# links = (a.attrib['href'] for a in root.iterdescendants('a')) 

	# how would I get the domains?
	# enumerate domains and relative links
	# once I have them, add to a set


		return links
