from locust import HttpLocust, TaskSet

def index(l):
    l.client.get("/")

def auth(l):
    l.client.post("/auth/anonymouslogin", {"device_id":"uuid92138123", "client_id":"AndroidDev0.1", "client_secret":"fd1ce5392d2c631b7891de37c3d2c52d"})

def offers(l):
    l.client.get("/offers", headers={"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkZXZpY2VfaWQiOiJ1dWlkOTIxMzgxMjMiLCJleHBpcmVkX3RpbWUiOiIyMDE1LTA3LTI2IDE0OjQyOjM0IiwicmVmcmVzaF90b2tlbiI6ImM0ZWYyNmRmOTYxMDY0NTI5ZDQzNGY3YmU5MWVhNDI3IiwiY2xpZW50X2lkIjoiQW5kcm9pZERldjAuMSIsImNsaWVudF9zZWNyZXQiOiJmZDFjZTUzOTJkMmM2MzFiNzg5MWRlMzdjM2QyYzUyZCJ9.KExb7Q4zik0_3pzhzTQ7i3WbqFnB3ES0DY7M5WFV-Mw"})

def cat(l):
    l.client.get("/categories")

def prodcat(l):
	l.client.get("/categories/465/products")

def product(l):
	l.client.get("/products/59881", headers={"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkZXZpY2VfaWQiOiJ1dWlkOTIxMzgxMjMiLCJleHBpcmVkX3RpbWUiOiIyMDE1LTA3LTI2IDE0OjQyOjM0IiwicmVmcmVzaF90b2tlbiI6ImM0ZWYyNmRmOTYxMDY0NTI5ZDQzNGY3YmU5MWVhNDI3IiwiY2xpZW50X2lkIjoiQW5kcm9pZERldjAuMSIsImNsaWVudF9zZWNyZXQiOiJmZDFjZTUzOTJkMmM2MzFiNzg5MWRlMzdjM2QyYzUyZCJ9.KExb7Q4zik0_3pzhzTQ7i3WbqFnB3ES0DY7M5WFV-Mw"})

def brands(l):
	l.client.get("/brands")

def location(l):
	l.client.get("/locations")

def me(l):
	l.client.get("/me", headers={"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkZXZpY2VfaWQiOiJ1dWlkOTIxMzgxMjMiLCJleHBpcmVkX3RpbWUiOiIyMDE1LTA3LTI2IDE0OjQyOjM0IiwicmVmcmVzaF90b2tlbiI6ImM0ZWYyNmRmOTYxMDY0NTI5ZDQzNGY3YmU5MWVhNDI3IiwiY2xpZW50X2lkIjoiQW5kcm9pZERldjAuMSIsImNsaWVudF9zZWNyZXQiOiJmZDFjZTUzOTJkMmM2MzFiNzg5MWRlMzdjM2QyYzUyZCJ9.KExb7Q4zik0_3pzhzTQ7i3WbqFnB3ES0DY7M5WFV-Mw"})

def search(l):
	l.client.get("/search?terms=asus", headers={"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkZXZpY2VfaWQiOiJ1dWlkOTIxMzgxMjMiLCJleHBpcmVkX3RpbWUiOiIyMDE1LTA3LTI2IDE0OjQyOjM0IiwicmVmcmVzaF90b2tlbiI6ImM0ZWYyNmRmOTYxMDY0NTI5ZDQzNGY3YmU5MWVhNDI3IiwiY2xpZW50X2lkIjoiQW5kcm9pZERldjAuMSIsImNsaWVudF9zZWNyZXQiOiJmZDFjZTUzOTJkMmM2MzFiNzg5MWRlMzdjM2QyYzUyZCJ9.KExb7Q4zik0_3pzhzTQ7i3WbqFnB3ES0DY7M5WFV-Mw"})

def searchsug(l):
	l.client.get("/search_suggestions?terms=asu", headers={"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkZXZpY2VfaWQiOiJ1dWlkOTIxMzgxMjMiLCJleHBpcmVkX3RpbWUiOiIyMDE1LTA3LTI2IDE0OjQyOjM0IiwicmVmcmVzaF90b2tlbiI6ImM0ZWYyNmRmOTYxMDY0NTI5ZDQzNGY3YmU5MWVhNDI3IiwiY2xpZW50X2lkIjoiQW5kcm9pZERldjAuMSIsImNsaWVudF9zZWNyZXQiOiJmZDFjZTUzOTJkMmM2MzFiNzg5MWRlMzdjM2QyYzUyZCJ9.KExb7Q4zik0_3pzhzTQ7i3WbqFnB3ES0DY7M5WFV-Mw"})	

class UserBehavior(TaskSet):
    tasks = {
    	auth:1, 
    	me: 1,
    	search: 1,
    	searchsug: 1,
    	offers:1, 
    	cat:1, 
    	prodcat:1,
    	product:1, 
    	brands:1, 
    	location:1
    }

#    def on_start(self):
#        login(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait=5000
    max_wait=9000