import re
from urlparse import urlparse
from bs4 import BeautifulSoup
import urllib2

class SiteParser:
	_sites = []

	_url = ''

	_tld = ''

	page = ''

	title = ''

	content = ''

	def __init__(self, fullUrl):
		self._url = fullUrl

		self._sites = [
			'detik',
			'kompas',
			'merdeka',
			'tempo',
		]

		self._tld = self.getHost()

		response = urllib2.urlopen(self._url)
		self.page = BeautifulSoup(response.read(), "html.parser")

	def getHost(self):
		return urlparse(self._url).netloc

	def getContentBySite(self):
		index = 0
		for i in range(0, len(self._sites)):
			if self._tld.find(self._sites[i]) is not -1:
				index = i
				break

		eval('self.' + self._sites[index] + '()')

	def kompas(self):
		h2s = self.page.find_all('h2')
		self.title = h2s[0].text
		
		#This is bullshit, try to get the text directly without having to loop in the elements
		for elem in self.page.find_all('div'):
			classes = elem.get('class')
			
			if (classes is not None):
				className = ' '.join(classes)
				if (className.strip() == 'span6 nml' or className.strip() == 'kcm-span6'):
					if (len(elem.find_all('p'))):
						for p in elem.find_all('p'):
							self.content += p.text.encode('ascii', 'ignore') + "\n\n"
					else:
						self.content = re.compile(r'<.*?>').sub('', str(elem.find('span')).decode('utf-8').encode('ascii', 'ignore').replace('<br/>', '\n'))
					break

	def detik(self):
		self.title = ''
		self.content = ''

	def merdeka(self):
		self.title = ''
		self.content = ''

	def tempo(self):
		h1s = self.page.find_all('div')
		self.title = h1s[1].text

		ps = self.page.find_all('p')
		self.content = self.content = re.compile(r'<.*?>').sub('', str(ps[1].find('span')).decode('utf-8').encode('ascii', 'ignore').replace('<br/>', '\n'))
		print self.content