from bs4 import BeautifulSoup
import urllib2

def iterate(categories, level):
	for category in categories:
		a = category.find('a')
		if a.get('href') == "#": continue

		print ("\t" * level) + a.get('href')
		sub = category.find('ul', 'level{}'.format(level))
		if sub is not None:
			level = level + 1
			
			subCategories = sub.find_all("li", "level{}".format(level))
			iterate(subCategories, level)
			level = level - 1

def main():
	host = "http://magento.mataharimall.net"
	response = urllib2.urlopen(host)
	pageSource = response.read()

	soup = BeautifulSoup(pageSource, 'html.parser')

	level = 0
	categories = soup.find_all("li", "level{}".format(level))
	iterate(categories, level)

if __name__ == '__main__':
	main()