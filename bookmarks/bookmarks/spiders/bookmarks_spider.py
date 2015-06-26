import scrapy

from ..lxml_bookmarks import linksects

class BookmarksSpider(scrapy.Spider):
	"""docstring for BookmarksSpider"""

	name = 'bkmks'
	links = linksects()

	allowed_domains = ["localhost://8000"]

	start_urls = [links[89]] #happens to be a wikipedia page on LDA

	def parse(self, response):
		filename = response.url.split("/")[-2] + '.html'
		with open(filename, 'wb') as f:
			f.write(response.body)




