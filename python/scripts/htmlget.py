from bs4 import BeautifulSoup
import urllib2


#response = urllib2.urlopen("https://www.mataharimall.com?c=uycrVZ")
response = urllib2.urlopen("https://aws.mataharimall.com")
page_source = response.read()

soup = BeautifulSoup(page_source, 'html.parser')

categories = soup("li","category-item")

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