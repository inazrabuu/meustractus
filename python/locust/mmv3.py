from locust import HttpLocust, TaskSet, task
from bs4 import BeautifulSoup
import random

class MMV3TaskSet(TaskSet):
	categoryFile = "v3.mataharimall.net.txt"

	categories = []

	endpoints = {
		'login_page' : '/user',
		'login_action' : '/user/ajax/login',
		'logout_action' : '/logout'
	}

	def on_start(self):
		if not len(self.categories) > 0 :
			#Get the categories from file
			with open(self.categoryFile, "r") as f:
				fread = f.read().decode('utf-16').encode('ascii', 'ignore')

			catlist = fread.splitlines(True)

			for line in catlist:
				self.categories.append(line.strip())

	@task(1)
	def index(self):
		self.client.get('/')

		self.client.get(self.endpoints['login_page'])

		param = {
			'email'		 	: 'arman.rizal@mataharimall.com',
			'passwd'		: 'arman123',
			'rememberme': ''
		}
		#loginResponse = self.client.post(self.endpoints['login_page'], param)

	@task(2)
	def browsing(self):
		#Go to a category page
		categoryPage = self.client.get(random.choice(self.categories))
		if categoryPage is not None:
			category = BeautifulSoup(categoryPage.content, "html.parser")
			
			product = category("div", "item-product-list")
			if len(product) > 0:
				
				urlPdp = random.choice(product).find('a')
				if urlPdp is not None:
					#Go to a Product Detail Page
					pdpPage = self.client.get(urlPdp.get("href"))

class MMV3User(HttpLocust):
	task_set = MMV3TaskSet
	min_wait = 5000
	max_wait = 9000