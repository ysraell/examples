
import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def day_to_hour(self):
        self.client.get('/dh/5')

    @task
    def day_to_minute(self):
        self.client.get('/dm/2')
        
