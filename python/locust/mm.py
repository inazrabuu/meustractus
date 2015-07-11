from locust import HttpLocust, TaskSet, task
from bs4 import BeautifulSoup
import random

class MMTaskSet(TaskSet):
	categories = []

	def on_start(self):
		if not len(self.categories) > 0 :
			with open("mataharimall.com.txt", "r") as f:
				fread = f.read().decode('utf-16').encode('ascii', 'ignore')

			catlist = fread.splitlines(True)

			for line in catlist:
				self.categories.append(line.strip())

	@task(1)
	def index(self):
		self.client.get("/")
	@task(2)
	def browsing(self):
		# Go to a category
		categoryPage = self.client.get(random.choice(self.categories))
		category = BeautifulSoup(categoryPage.content, "html.parser")
		urlPdp = random.choice(category("div", "item-product-list")).find('a')#
		if urlPdp is not None:
			# Go to a product detail page
			pdpPage = self.client.get(urlPdp.get('href'))
			if pdpPage is not None:
				pdp =  BeautifulSoup(pdpPage.content, "html.parser")
				form = pdp("form", "commerce-add-to-cart")
				inputs = form[0].find_all('input')
				for inp in inputs:
					print inp.get('name'), '=', inp.get('value'), "\n"
#	def login(self):

	
class MMUser(HttpLocust):
	task_set = MMTaskSet
	min_wait = 5000
	max_wait = 9000