from locust import HttpLocust, TaskSet, task
from bs4 import BeautifulSoup
import random

class MMV2TaskSet(TaskSet):
	endpoints = {
		'home' : '/',
		'login' : ''	
	}

	categoryFile = "v2categories.txt"
	categories = []

	def on_start(self):
		if not len(self.categories) > 0:
			with open(self.categoryFile, "r") as f:
				fread = f.read().decode('utf-16').encode('ascii', 'ignore')

			catlist = fread.splitlines(True)

			for line in catlist:
				self.categories.append(line.strip())

	@task(1)
	def scenario1(self):
		self.client.get(self.endpoints['home'])

	@task(2)
	def scenario2(self):
		self.client.get(self.endpoints['home'])

		categoryPage = self.client.get(random.choice(self.categories))

class MMV2User(HttpLocust):
	task_set = MMV2TaskSet
	min_wait = 5000
	max_wait = 9000
