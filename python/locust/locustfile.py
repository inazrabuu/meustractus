from locust import HttpLocust, TaskSet
from bs4 import BeautifulSoup

def index(l):
    with open("htmlget.txt", "r") as f:
        fread = f.read().decode('utf-16').encode('ascii', 'ignore')

	myList = fread.splitlines(True)

	for line in myList:
		l.client.get(line.strip() + "?c=uycrVZ")


class UserBehavior(TaskSet):
    tasks = {
        index
    }

#    def on_start(self):
#        login(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait=5000
    max_wait=9000