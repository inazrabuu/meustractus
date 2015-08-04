from locust import HttpLocust, TaskSet, task
from bs4 import BeautifulSoup
import random
import json
from pprint import pprint
from inspect import getmembers

class MMTaskSet(TaskSet):
	categories = []

	endpoints = {
		'cart' : '/cart',
		'add_to_cart' : '/system/ajax'
	}

	#categoryFile = "mataharimall.com.txt"
	categoryFile = "v3.mataharimall.net.txt"

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
		self.client.get("/")

	@task(2)
	def browsing(self):
		# Go to a category
		categoryPage = self.client.get(random.choice(self.categories))
		if categoryPage is not None:
			category = BeautifulSoup(categoryPage.content, "html.parser")
			urlPdp = random.choice(category("div", "item-product-list")).find('a')#
#			if urlPdp is not None:
#				# Go to a product detail page
#				pdpPage = self.client.get(urlPdp.get('href'))
#				if pdpPage is not None:
#					pdp =  BeautifulSoup(pdpPage.content, "html.parser")
#					form = pdp("form", "commerce-add-to-cart")
#					inputs = form[0].find_all('input')
#					param = {
#						"_triggering_element_value" : "Beli Aja",
#						"quantity" : 1
#					}
#					for inp in inputs:
#						if inp.get('name') == 'product_id' or inp.get('name') == 'form_id' or inp.get('name') == 'form_build_id':
#							param[inp.get('name')] = inp.get('value')#
#					# Put an item into shopping cart
#					atcResponse = self.client.post(self.endpoints['add_to_cart'], param)
#					
#					# View the cart
#					cartResponse = self.client.get(self.endpoints['cart'])
#					print cartResponse.content

	def login(self):

	
class MMUser(HttpLocust):
	task_set = MMTaskSet
	min_wait = 5000
	max_wait = 9000