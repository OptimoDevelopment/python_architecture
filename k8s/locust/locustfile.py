from locust import HttpLocust, TaskSet, task


class StalkerTaskSet(TaskSet):
    @task(1)
    def get_angelinas_orders(self):
        self.client.get("/api/orders/search/", params={'client_id': 1})

class DemoLocust(HttpLocust):
    task_set = StalkerTaskSet
    min_wait = 100
    max_wait = 1500
