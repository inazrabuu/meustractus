from locust import HttpLocust, TaskSet, task
from bs4 import BeautifulSoup
import random
import json
from pprint import pprint
from inspect import getmembers

class SCTaskSet(TaskSet):
	categories = []

	param = []

	endpoints = {
		'home' : '/login',
		'login' : '/login_check',
		'logout' : '/logout',
		'dashboard' : '/store/{}',
		'orders' : '/orders',
		'product' : '/products'
	}

	storeId = 499
		
	def on_start(self):
		loginRespone = self.client.get(self.endpoints['home'])
		loginPage = BeautifulSoup(loginRespone.content, "html.parser")

		self.param = {
			'_username' : 'retail.fashion@mataharimall.com',
			'_password' : 'karawaci'
		}

		inputs = loginPage.findAll('input')
		for inp in inputs:
			if inp.get('name') == '_csrf_token':
				self.param[inp.get('name')] = inp.get('value')

	#Login -> select store -> Dashbooard -> Logout 
	@task(1)
	def scenario1(self):
		self.client.post(self.endpoints['login'], self.param)
		
		self.client.get(self.endpoints['dashboard'].format(self.storeId))
		
		self.client.get(self.endpoints['logout'])

	#Login -> select store -> Dashboard -> orders -> view all statuses -> Logout
	@task(2)
	def scenario2(self):
		self.client.post(self.endpoints['login'], self.param)
		
		self.client.get(self.endpoints['dashboard'].format(self.storeId))

		statuses = ['pending', 'shipped', 'rejected', 'delivered']
		orderURL = self.endpoints['dashboard'].format(self.storeId) + self.endpoints['orders']

		self.client.get(orderURL)
		for status in statuses:
			self.client.get(orderURL + '?status={}'.format(status))

		self.client.get(self.endpoints['logout'])

	#Login -> select store -> Dashboard -> all products
	@task(2)
	def scenario3(self):
		self.client.post(self.endpoints['login'], self.param)

		self.client.get(self.endpoints['dashboard'].format(self.storeId))

		productURL = self.endpoints['dashboard'].format(self.storeId) + self.endpoints['product']

		self.client.get(productURL)

		self.client.get(self.endpoints['logout'])

	
class SCUser(HttpLocust):
	task_set = SCTaskSet
	min_wait = 5000
	max_wait = 9000