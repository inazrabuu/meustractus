from locust import HttpLocust, TaskSet, task
from bs4 import BeautifulSoup
import re

class MMAdminTask(TaskSet):
	endpoints = {
		'home' : '/',
		'login' : '/auth/auth/login',
		'logout': '/auth/logout'
	}

	#login > logout
	@task(1)
	def scenario1(self):
		homeResponse = self.client.get(self.endpoints['home'])
		
		home = BeautifulSoup(homeResponse.content, 'html.parser')

		param = {
			'email' : 'admin@mataharimall.com',
			'password' : '123456',
		}

		for inpute in home.find_all('input'):
			if (inpute.get('type') == 'hidden'):
				param[inpute.get('name')] = inpute.get('value')

		#login
		loginResponse = self.client.post(self.endpoints['home'], param)

		loginPage = BeautifulSoup(loginResponse.content, 'html.parser')
		for link in loginPage.find_all('a'):
			#if ("http:" in link.get('href')):
				print link.get('href')

		#logout
		logoutResponse = self.client.get(self.endpoints['logout'])		

class MMAdminUser(HttpLocust):
	task_set = MMAdminTask
	min_wait = 5000
	max_wait = 9000