 #!/usr/bin/python
 # -*- coding: utf-8 -*-
import re

#python 2.7 DON'T FORGET

# get links out of bookmarks.html

# regex from here http://daringfireball.net/2010/07/improved_regex_for_matching_urls

href = re.compile(r"""(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))""")

bookmarks = open('bookmarks.html') # this is the html file exported from Chrome.

#return lines containing a url
url_lines = (line for line in bookmarks if re.search(href, line))

#get just the links.
links = (re.search(href, link) for link in url_lines)

for link in links:
	print link.group()


"""
could do 
links = (re.search(href, link) for link in bookmarks if re.search(href, link))
but that's not so readable.
"""

