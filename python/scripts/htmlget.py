from bs4 import BeautifulSoup
import urllib2

def iterate(categories, level):
	for category in categories:
		tab = "\t" * level
		print "%s %s" % (tab, category.find("a").get("href"))
		subcats = category("li")
		if (len(subcats) > 0):
			iterate(subcats, level + 1)
			

def main():
	host = "http://v3.mataharimall.net"
	#host = raw_input("Please enter the MM host name (complete with the protocol): ")
	response = urllib2.urlopen(host)
	page_source = response.read()

	soup = BeautifulSoup(page_source, 'html.parser')

	categories = soup("li","category-item")

#	iterate(categories, 0)

	for category in categories:
		print (category.find("a").get('href'))
		subcats = category("li", "subcategory-item")
		
		if (len(subcats) > 0):
			for subcat in subcats:
				print ("\t" + subcat.find("a").get('href'))
				ssubcats = subcat("li")
				if (len(ssubcats) > 0):
					for ssubcat in ssubcats:
						print ("\t\t" + subcat.find("a").get('href'))

if __name__ == '__main__':
	main()