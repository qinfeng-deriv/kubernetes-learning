from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)  # Time between requests in seconds

    @task
    def my_task(self):
        self.client.get("/")

